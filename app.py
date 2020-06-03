import constants


def begin_app():
    print('BASTEKBALL TEAM STATS TOOL\n')
    print('---- MENU ----\n')
    print('Here are your choices:')
    print('\nDisplay Team Stats:')
    for team in constants.TEAMS:
        print(f'Enter {constants.TEAMS.index(team) + 1} for {team}')
    print('\nAny other key - Quit')
    choice = input('Enter an option:\n > ')
    try:
        return int(choice) - 1
    except ValueError:
        return - 1


begin_app()
