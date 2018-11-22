import axios from 'axios'
// axios.defaults.headers.common['token'] = 'valuexyz'

const loginURL = '/api/v1/get_auth_token'
const competitionsURL = '/api/v1/competitions/'
const matchesURL = '/api/v1/matches/'
const opponentsURL = '/api/v1/opponents/'
const playerMatchesURL = '/api/v1/playermatches/'
const matchStatsURL = '/api/v1/matchstats/'
const playersURL = '/api/v1/players/'
const shotsURL = '/api/v1/shots/'

const getHeader = function () {
  // todo : get this from store instead?
  const futUser = JSON.parse(window.localStorage.getItem('futUser'))
  const headers = {
    'Authorization': 'Bearer ' + futUser.token
  }
  return headers
}

export default {
  logIn (username, password) {
    return axios.post(loginURL, {username: username, password: password})
      .then(response => response.data)
  },
  //  competitions
  getCompetitions () {
    return axios.get(competitionsURL, {headers: getHeader()})
      .then(response => response.data)
  },
  getCompetition (id) {
    return axios.get(`${competitionsURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  createCompetition (competition) {
    return axios.post(competitionsURL, competition, {headers: getHeader()})
      .then(response => response.data)
  },
  updateCompetition (id, competition) {
    return axios.patch(`${competitionsURL}/${id}`, competition, {headers: getHeader()})
      .then(response => response.data)
  },
  deleteCompetition (id) {
    return axios.delete(`${competitionsURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  //  matches
  getMatchesByCompetition (id) {
    return axios.get(`${matchesURL}/?competition_id=${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  getMatchesByOpponent (id) {
    return axios.get(`${matchesURL}/?opponent_id=${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  // Match
  getMatch (id) {
    return axios.get(`${matchesURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  createMatch (match) {
    return axios.post(matchesURL, match, {headers: getHeader()})
      .then(response => response.data)
  },
  updateMatch (id, match) {
    return axios.patch(`${matchesURL}/${id}`, match, {headers: getHeader()})
      .then(response => response.data)
  },
  deleteMatch (id) {
    return axios.delete(`${matchesURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  // MatchStats  ( no return, data is accessed on match? )
  getMatchStats (id) {
    return axios.get(`${matchStatsURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  createMatchStats (match_stats) {
    return axios.post(matchStatsURL, match_stats, {headers: getHeader()})
      .then(response => response.data)
  },
  updateMatchStats (id, match) {
    return axios.patch(`${matchStatsURL}/${id}`, match, {headers: getHeader()})
      .then(response => response.data)
  },
  // Opponents
  getOpponents () {
    return axios.get(opponentsURL, {headers: getHeader()})
      .then(response => response.data)
  },
  getOpponent (id) {
    return axios.get(`${opponentsURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  createOpponent (opponent) {
    return axios.post(opponentsURL, opponent, {headers: getHeader()})
      .then(response => response.data)
  },
  updateOpponent (id, opponent) {
    return axios.patch(`${opponentsURL}/${id}`, opponent, {headers: getHeader()})
      .then(response => response.data)
  },
  deleteOpponent (id) {
    return axios.delete(`${opponentsURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  // playerMatches
  createPlayerMatch (player_match) {
    return axios.post(playerMatchesURL, player_match, {headers: getHeader()})
      .then(response => response.data)
  },
  updatePlayerMatch (id, player_match) {
    return axios.patch(`${playerMatchesURL}/${id}`, player_match, {headers: getHeader()})
      .then(response => response.data)
  },
  deletePlayerMatch (id) {
    return axios.delete(`${playerMatchesURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  getPlayerMatchesByMatch (id) {
    return axios.get(`${playerMatchesURL}/?match_id=${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  getPlayerMatchesByCompetition (id) {
    return axios.get(`${playerMatchesURL}/?competition_id=${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  getPlayerMatchesByOpponent (id) {
    return axios.get(`${playerMatchesURL}/?opponent_id=${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  getPlayerMatchesByPlayer (id) {
    return axios.get(`${playerMatchesURL}/?player_id=${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  getPlayerMatchesByPlayerEx (id) {
    return axios.get(`${playerMatchesURL}/?player_id=${id}&expand=true`, {headers: getHeader()})
      .then(response => response.data)
  },

  // players
  getPlayers () {
    return axios.get(playersURL, {headers: getHeader()})
      .then(response => response.data)
  },
  getPlayer (id) {
    return axios.get(`${playersURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  createPlayer (player) {
    return axios.post(playersURL, player, {headers: getHeader()})
      .then(response => response.data)
  },
  updatePlayer (id, player) {
    return axios.patch(`${playersURL}/${id}`, player, {headers: getHeader()})
      .then(response => response.data)
  },
  deletePlayer (id) {
    return axios.delete(`${playersURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  // shots
  getShotsByMatch (id) {
    return axios.get(`${shotsURL}/?match_id=${id}`, {headers: getHeader()})
      .then(response => response.data)
  },
  // todo: is this even used?
  getShotsByMatchEx (id) {
    return axios.get(`${shotsURL}/?match_id=${id}&expand=true`, {headers: getHeader()})
      .then(response => response.data)
  },
  createShot (shot) {
    if (shot.id === -1) { delete shot.id }

    return axios.post(shotsURL, shot, {headers: getHeader()})
      .then(response => response.data)
  },
  updateShot (id, shot) {
    return axios.patch(`${shotsURL}/${id}`, shot, {headers: getHeader()})
      .then(response => response.data)
  },
  deleteShot (id) {
    return axios.delete(`${shotsURL}/${id}`, {headers: getHeader()})
      .then(response => response.data)
  }

}
