# Garden Advice Generator
# This script provides gardening advice based on the season and type of plant.

# Advice dictionaries
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}

SEASON_PLANT_RECOMMENDATIONS = {
    "summer": ["sunflowers", "basil", "tomatoes"],
    "winter": ["kale", "spinach", "pansies"],
}


def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    return "No advice for this season."


def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    return "No advice for this type of plant."


def generate_advice(season, plant_type):
    return get_season_advice(season) + "\n" + get_plant_advice(plant_type)


if __name__ == "__main__":
    season = input("Enter the season: ").lower()
    plant_type = input("Enter the type of plant: ").lower()
    print(generate_advice(season, plant_type))

