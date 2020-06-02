# Import player data
import constants

# Clean up the player information
def player_info(player):
    # Create a new empty dictionary
    player_info = {}
    # Bring over player name to new list
    player_info['name'] = player['name']
    # Bring over player guardians to new list
    player_info['guardians'] = player['guardians']
    # Convert height to an interger
    player_info['height'] = int(player['height'].replace(' inches', ''))
    # Convert experience to a boolean value
    if player['experience'] == 'YES':
        player_info['experience'] = True
    else:
        player_info['experience'] = False
    # Return new player info
    return player_info


# Create a clean_data function

# Create a balance_teams function


# Display stats
