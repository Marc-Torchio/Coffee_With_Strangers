class Stranger:
    def __init__(self, kp_email, first_name, last_name, team, pause = 'No', previous_matches=None):
        """
        Initialize a new Strangers object.

        Parameters:
        kp_email (str): The KP email of the stranger.
        first_name (str): The first name of the stranger.
        last_name (str): The last name of the stranger.
        team (str): The team of the stranger.
        previous_matches (dict): A dictionary of previous matches, defaults to an empty dictionary if not provided.
        """
        self.kp_email = kp_email
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.pause = pause
        self.previous_matches = previous_matches if previous_matches is not None else []