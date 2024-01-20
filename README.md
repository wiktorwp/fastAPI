# Simple teams lineup maker with python fastAPI

This app randomly generates lineups for the knockout stage of footbal cup with given teams data in a JSON format

# Endpoints

## `POST /lineup`

Creates the lineups of given teams and returns them.

### Sample data
```json
{
    "teams": [
        {"name": "Manchester City", "country": "EN", "placement": 1, "previous_group": "A"},
        {"name": "Paris Saint-Germain", "country": "FR", "placement": 2, "previous_group": "A"},
        {"name": "Liverpool", "country": "EN", "placement": 1, "previous_group": "B"},
        {"name": "Atlético Madryt", "country": "ES", "placement": 2, "previous_group": "B"},
        {"name": "AJAX", "country": "NED", "placement": 1, "previous_group": "C"},
        {"name": "Sporting CP", "country": "POR", "placement": 2, "previous_group": "C"},
        {"name": "Real Madryt", "country": "ES", "placement": 1, "previous_group": "D"},
        {"name": "Inter Mediolan", "country": "IT", "placement": 2, "previous_group": "D"},
        {"name": "Bayern Monachium", "country": "DE", "placement": 1, "previous_group": "E"},
        {"name": "SL Benfica", "country": "POR", "placement": 2, "previous_group": "E"},
        {"name": "Manchester United", "country": "EN", "placement": 1, "previous_group": "F"},
        {"name": "Villarreal CF", "country": "ES", "placement": 2, "previous_group": "F"},
        {"name": "Lille OSC", "country": "FR", "placement": 1, "previous_group": "G"},
        {"name": "Red Bull Salzburg", "country": "AU", "placement": 2, "previous_group": "G"},
        {"name": "Juventus", "country": "IT", "placement": 1, "previous_group": "H"},
        {"name": "Chelsea", "country": "EN", "placement": 2, "previous_group": "H"}
    ]
}
```

### Sample response
```json
[
    [
        "Manchester City",
        "Lille OSC"
    ],
    [
        "Paris Saint-Germain",
        "Chelsea"
    ],
    [
        "Liverpool",
        "Bayern Monachium"
    ],
    [
        "Atlético Madryt",
        "SL Benfica"
    ],
    [
        "AJAX",
        "Real Madryt"
    ],
    [
        "Sporting CP",
        "Villarreal CF"
    ],
    [
        "Inter Mediolan",
        "Red Bull Salzburg"
    ],
    [
        "Manchester United",
        "Juventus"
    ]
]
```

## `GET /lineup`

Retrieves the earlier created lineups.  
If no lineups were created, returns an empty array.

### Sample response
```json
[
    [
        "Manchester City",
        "Lille OSC"
    ],
    [
        "Paris Saint-Germain",
        "Chelsea"
    ],
    [
        "Liverpool",
        "Bayern Monachium"
    ],
    [
        "Atlético Madryt",
        "SL Benfica"
    ],
    [
        "AJAX",
        "Real Madryt"
    ],
    [
        "Sporting CP",
        "Villarreal CF"
    ],
    [
        "Inter Mediolan",
        "Red Bull Salzburg"
    ],
    [
        "Manchester United",
        "Juventus"
    ]
]
```

## `GET /lineup/{team_name}`

Retrieves the opponent of the given team.  
If team doesn't exist, returns "No such team found"

### Sample request
```
GET /lineup/Chelsea
```

### Sample Response
```
"Paris Saint-Germain"
```

## `PATCH /lineup`

Rerolls the lineup of earlier given teams and returns it.

### Sample response
```json
[
    [
        "Manchester City",
        "Bayern Monachium"
    ],
    [
        "Paris Saint-Germain",
        "SL Benfica"
    ],
    [
        "Liverpool",
        "Juventus"
    ],
    [
        "Atlético Madryt",
        "Red Bull Salzburg"
    ],
    [
        "AJAX",
        "Real Madryt"
    ],
    [
        "Sporting CP",
        "Villarreal CF"
    ],
    [
        "Inter Mediolan",
        "Chelsea"
    ],
    [
        "Manchester United",
        "Lille OSC"
    ]
]
```
