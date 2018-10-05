from marshmallow import fields
from flask_marshmallow.sqla import ModelSchema
from .shared import ma
from .shared import api
from .models import *


class UserSchema(ModelSchema):
    is_editor = fields.Boolean(dump_only=True)

    class Meta:
        strict = True
        model = User
        fields = ('username', 'is_editor', 'teams')  # token here?
        sqla_session = db.session


class TeamSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeleteTeam'.lower(), team_id="<id>"),
         'collection': ma.URLFor('CreateListTeam'.lower(), ),
         })

    class Meta:
        strict = True
        model = Team
        sqla_session = db.session


class TeamSchemaEx(TeamSchema):
    matches = fields.Nested('MatchSchema', many=True, dump_only=True)
    players = fields.Nested('PlayerSchema', many=True, dump_only=True)


class PlayerSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeletePlayer'.lower(), player_id="<id>"),
         'collection': ma.URLFor('CreateListPlayer'.lower()),
         })

    label = fields.String(dump_only=True)
    num_apps =  fields.Integer(dump_only=True)

    class Meta:
        strict = True
        model = Player
        sqla_session = db.session
        exclude = ["player_matches",]


class PlayerSchemaEx(PlayerSchema):
    player_matches = fields.Nested('PlayerMatchSchemaEx', many=True,
                                   dump_only=True)

    team = fields.Nested('TeamSchema', dump_only=True,
                         exclude=("matches", "players"))


class CompetitionSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeleteCompetition'.lower(),
                           competition_id="<id>"),
         'collection': ma.URLFor('CreateListCompetition'.lower())})

    start_date = fields.String(dump_only=True)
    num_match_won = fields.String(dump_only=True)
    num_match_tied = fields.String(dump_only=True)
    num_match_lost = fields.String(dump_only=True)
    match_results = fields.String(dump_only=True)
    goal_differential = fields.Integer(dump_only=True)

    class Meta:
        strict = True
        model = Competition
        sqla_session = db.session
        exclude = ["matches",]


class CompetitionSchemaEx(CompetitionSchema):
    matches = fields.Nested('MatchSchemaEx', many=True, dump_only=True,
                            exclude=("player_matches",))


class OpponentSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeleteOpponent'.lower(), opponent_id="<id>"),
         'collection': ma.URLFor('CreateListOpponent'.lower())})

    num_match_won = fields.String(dump_only=True)
    num_match_tied = fields.String(dump_only=True)
    num_match_lost = fields.String(dump_only=True)
    match_results = fields.String(dump_only=True)
    goal_differential = fields.Integer(dump_only=True)

    class Meta:
        strict = True
        model = Opponent
        sqla_session = db.session
        exclude = ["matches",]


class OpponentSchemaEx(OpponentSchema):
    matches = fields.Nested('MatchSchemaEx', many=True, dump_only=True,
                            exclude=("player_matches", "opponent", "team"))


class ShotSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeleteShot'.lower(), shot_id="<id>"),
         'collection': ma.URLFor('CreateListShot'.lower())})

    scored = fields.Boolean(dump_only=True)

    class Meta:
        strict = True
        model = Shot
        sqla_session = db.session


class ShotSchemaEx(ShotSchema):
    goal = fields.Nested('GoalSchemaEx', dump_only=True,
                         exclude=["shot", "player_match"])

    player_match = fields.Nested('PlayerMatchSchemaEx', dump_only=True,
                                 exclude=["shots"])


class AssistSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeleteAssist'.lower(), assist_id="<id>"),
         'collection': ma.URLFor('CreateListAssist'.lower())
         })

    class Meta:
        strict = True
        model = Assist
        sqla_session = db.session


class AssistSchemaEx(AssistSchema):
    player_match = fields.Nested('PlayerMatchSchemaEx', dump_only=True,
                                 exclude=["assists"])

    goal = fields.Nested('GoalSchemaEx', dump_only=True,
                         exclude=["assist", "player_match"])


class GoalSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeleteGoal'.lower(), goal_id="<id>"),
         'collection': ma.URLFor('CreateListGoal'.lower())
         })

    class Meta:
        strict = True
        model = Goal
        sqla_session = db.session


class GoalSchemaEx(GoalSchema):
    assist = fields.Nested('AssistSchemaEx', dump_only=True, exclude=["goal", ])
    shot = fields.Nested('ShotSchemaEx', dump_only=True, exclude=["goal", ])


class PlayerMatchSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeletePlayerMatch'.lower(),
                           playermatch_id="<id>"),
         'collection': ma.URLFor('CreateListPlayerMatch'.lower()),
         })

    # hybrid properties on model
    player_label = fields.String(dump_only=True)
    num_shots = fields.Integer(dump_only=True)
    num_shots_against = fields.Integer(dump_only=True)
    num_goals = fields.Integer(dump_only=True)
    num_goals_against = fields.Integer(dump_only=True)
    num_assists = fields.Integer(dump_only=True)
    num_saves = fields.Integer(dump_only=True)

    class Meta:
        strict = True
        model = PlayerMatch
        sqla_session = db.session
        exclude = ("assists", "shots")


class PlayerMatchSchemaEx(PlayerMatchSchema):
    #player = fields.Nested(PlayerSchemaEx, dump_only=True,
    #                       exclude=("player_matches", "team"))
    match = fields.Nested('MatchSchemaEx', dump_only=True,
                          only=("id",
                                "date_time",
                                "competition_name",
                                "competition_id",
                                "opponent_name",
                                "opponent_id",
                                "result",
                                "score"))
                          #exclude=("player_matches", "team"))
    #shots = fields.Nested(ShotSchema, dump_only=True, many=True)
    #assists = fields.Nested(AssistSchema, dump_only=True, many=True)
    # goals = fields.Nested(GoalSchema, dump_only=True, many=True)



class MatchStatsSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeleteMatchStats'.lower(),
                           matchstats_id="<id>"),
         'collection': ma.URLFor('CreateListMatchStats'.lower()),
         })

    class Meta:
        strict = True
        model = MatchStats
        sqla_session = db.session


class MatchSchema(ModelSchema):
    _links = ma.Hyperlinks(
        {'self': ma.URLFor('GetUpdateDeleteMatch'.lower(), match_id="<id>"),
         'collection': ma.URLFor('CreateListMatch'.lower()),
         })

    # add hybrid properties on model
    result = fields.String(dump_only=True)
    score = fields.String(dump_only=True)
    result_long = fields.String(dump_only=True)
    num_goals = fields.Integer(dump_only=True)
    num_goals_against = fields.Integer(dump_only=True)
    goal_differential = fields.Integer(dump_only=True)

    # add hybrid properties from MatchStats for convenient access
    opponent_name = fields.String(dump_only=True)
    competition_name = fields.String(dump_only=True)
    goals_timeline = fields.List(fields.String, dump_only=True, )
    goals_against_timeline = fields.List(fields.String, dump_only=True, )
    num_shots = fields.Integer(dump_only=True)
    num_shots_against = fields.Integer(dump_only=True)
    shot_on_target_pct = fields.String(dump_only=True)
    opponent_shot_on_target_pct = fields.String(dump_only=True)
    num_corners = fields.Integer(dump_only=True)
    num_opponent_corners = fields.Integer(dump_only=True)
    num_yellow_cards = fields.Integer(dump_only=True)
    num_opponent_yellow_cards = fields.Integer(dump_only=True)
    num_red_cards = fields.Integer(dump_only=True)
    num_opponent_red_cards = fields.Integer(dump_only=True)
    num_passes = fields.Integer(dump_only=True)
    num_opponent_passes = fields.Integer(dump_only=True)
    num_pass_strings = fields.Integer(dump_only=True)
    num_opponent_pass_strings = fields.Integer(dump_only=True)
    pass_pct = fields.Integer(dump_only=True)
    opponent_pass_pct = fields.Integer(dump_only=True)

    class Meta:
        strict = True
        model = Match
        sqla_session = db.session


class MatchSchemaEx(MatchSchema):
    competition = fields.Nested(CompetitionSchema, dump_only=True,
                                exclude=("matches",))

    opponent = fields.Nested(OpponentSchema, dump_only=True,
                             exclude=("matches",))

    team = fields.Nested(TeamSchema, dump_only=True,
                         exclude=("players", "matches", "opponents",
                                  "competitions", "teams"))

    match_stats = fields.Nested(MatchStatsSchema, dump_only=True)

    player_matches = fields.Nested(PlayerMatchSchemaEx, dump_only=True,
                                   many=True, exclude=("match",))
