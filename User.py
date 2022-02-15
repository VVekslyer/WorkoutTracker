
class User:
    def __init__(self, name, email, goals, level, weight, height, *args, **kwargs):
        
        self.name = name
        self.email = email
        self.goals = []              # Hypertrophy, Strength, Performance
        self.level = level           # Beginner, Intermidiate, Advanced
        self.custom_workouts = []    # A list of lists of workouts
        self.unit_of_weight = "LBS"  # Can be LBS or KG
        self.unit_of_height = "FT"   # Can be ft. or cm
        self.weight = weight
        self.height = height

