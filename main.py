import random


class Team:
    def __init__(self, name, country, placement, previous_group):
        self.name = name
        self.country = country
        self.placement = placement
        self.previous_group = previous_group


def create_playability_matrix(teams_array):
    matrix = {}
    for team in teams_array:
        matrix[team.name] = {}
        for counter_team in teams_array:
            if counter_team.country == team.country \
                    or counter_team.placement != team.placement \
                    or counter_team.previous_group == team.previous_group:
                matrix[team.name][counter_team.name] = 0
            else:
                matrix[team.name][counter_team.name] = 1
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
        for counter_team in value:
            new_playability_matrix[entry].append(counter_team)

    return new_playability_matrix


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

print(convert_to_table(map_only_playable(create_playability_matrix(teams))))
