import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Team:
    def __init__(self, name, country, placement, previous_group):
        self.name = name
        self.country = country
        self.placement = placement
        self.previous_group = previous_group


class TeamModel(BaseModel):
    name: str
    country: str
    placement: int
    previous_group: str


class TeamsArrayModel(BaseModel):
    teams: list[TeamModel]


def create_playability_matrix(teams_array):
    matrix = {}
    for team in teams_array:
        matrix[team.name] = {}
        for opponent in teams_array:
            if opponent.country == team.country \
                    or opponent.placement == team.placement \
                    or opponent.previous_group == team.previous_group:
                matrix[team.name][opponent.name] = 0
            else:
                matrix[team.name][opponent.name] = 1
    return matrix


def filter_playable(team_playability_matrix):
    entry, value = team_playability_matrix
    if value == 0:
        return False
    else:
        return True


def map_only_playable(playability_matrix):
    for entry, value in playability_matrix.items():
        playability_matrix[entry] = dict(filter(filter_playable, value.items()))
    return playability_matrix


def convert_to_table(playability_matrix):
    new_playability_matrix = {}
    for entry, value in playability_matrix.items():
        new_playability_matrix[entry] = []
        for opponent in value:
            new_playability_matrix[entry].append(opponent)

    return new_playability_matrix


def opponent_random_choice(playability_arrays):
    final_array = []
    chosen_teams = []
    for entry, value in playability_arrays.items():
        if entry not in chosen_teams:
            opponent = random.choice(value)
            while opponent in chosen_teams:
                opponent = random.choice(value)
            else:
                final_array.append((entry, opponent))
                chosen_teams.append(opponent)
                chosen_teams.append(entry)
    return final_array


teams = [
    Team("Manchester City", "EN", 1, "A"),
    Team("Paris Saint-Germain", "FR", 2, "A"),
    Team("Liverpool", "EN", 1, "B"),
    Team("Atlético Madryt", "ES", 2, "B"),
    Team("AJAX", "NED", 1, "C"),
    Team("Sporting CP", "POR", 2, "C"),
    Team("Real Madryt", "ES", 1, "D"),
    Team("Inter Mediolan", "IT", 2, "D"),
    Team("Bayern Monachium", "DE", 1, "E"),
    Team("SL Benfica", "POR", 2, "E"),
    Team("Manchester United", "EN", 1, "F"),
    Team("Villarreal CF", "ES", 2, "F"),
    Team("Lille OSC", "FR", 1, "G"),
    Team("Red Bull Salzburg", "AU", 2, "G"),
    Team("Juventus", "IT", 1, "H"),
    Team("Chelsea", "EN", 2, "H")
]

lineup = []
saved_teams = []


# Creates new lineup array and returns it
@app.post("/lineup")
async def create_teams_lineup(teams_array_model: TeamsArrayModel):
    global lineup
    global saved_teams
    saved_teams = teams_array_model.teams
    lineup = opponent_random_choice(
        convert_to_table(map_only_playable(create_playability_matrix(teams_array_model.teams))))
    return lineup


@app.get("/lineup")
async def get_teams_lineup():
    global lineup
    return lineup


@app.get("/lineup/{team_name}")
async def get_team_lineup(team_name: str):
    for team_lineup in lineup:
        if team_name in team_lineup:
            if team_lineup[0] == team_name:
                return team_lineup[1]
            else:
                return team_lineup[0]

    return "No such team found"


@app.patch("/lineup")
async def reroll_teams_lineup():
    global lineup
    lineup = opponent_random_choice(
        convert_to_table(map_only_playable(create_playability_matrix(saved_teams))))
    return lineup

print(opponent_random_choice(convert_to_table(map_only_playable(create_playability_matrix(teams)))))
