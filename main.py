import random 
from time import sleep 

test_8 = ["Jets", "Hawks", "Coyotes", "Leopards", "Lions", "Warriors", "Mules", "Lunas"] # 8 teams
test_16 = ["Jets", "Hawks", "Coyotes", "Leopards", "Lions", "Warriors", "Mules", "Lunas", 
           "Falcons", "Menehunes", "Koa", "Raiders", "Gladiators", "Tigers", "Sharks", "Bulls"] # 16 teams
league_name = ['My League'] # league name
games = 16 # number of games

teams = [] # list of teams in the league
div1 = [] # division 1
div2 = [] # division 2
div3 = [] # division 3
div4 = [] # division 4

remaining = [] # remaining teams to be assigned to a division

# subprocess.call(["afplay", "high_hat.wav"])

# d = {'Patriots' : 'Brady', 'Chiefs' : 'Mahomes', 'Warriors' : 'Curry'}
# while d:
#     key, value = d.popitem()
#     print(key, '-->', value)


def round_robin(teamshere, rounds): # round robin function
    # bye
    if len(teamshere) % 2: # odd number of teams
        teamshere.append(None) # add a bye

    schedule = [] # schedule
    for tor in range(rounds): # for each round
        matchups = [] # matchups
        length = len(teamshere) # length of the teams
        for i in range(int(length / 2)): # for each team
            pairing = (teamshere[i], teamshere[len(teamshere) - i - 1]) # pairing
            # alternate first team
            if i == 0 and tor % 2: # odd round
                pairing = pairing[::-1] # reverse the pairing
            # alternate based on the team's previous round appearance
            if schedule and None not in pairing:
                previous_round = list(sum(schedule[-1], ())) # flatten the schedule
                for team in pairing: # for each team
                    if team in previous_round and pairing[previous_round.index(team) % 2] == team: # if the team is in the previous round
                        pairing = pairing[::-1] # reverse the pairing
            matchups.append(pairing)    # add the pairing to the matchups
        teamshere.insert(1, teamshere.pop()) # rotate the teams
        schedule.append(matchups) # add the matchups to the schedule

    return schedule # return the schedule

# des = round_robin(test_16, 10)
#
# counted = 1
# for matchup in des:
#     print("{} - {}".format(counted, matchup))
#     print(" ")
#     counted = counted + 1


def main():
    print("")
    print("_________________________")
    print("Current League Name: " + ', '.join(league_name) + "\n") # print the current league name
    print("CURRENT OPTIONS: ")
    print("_________________________")
    print("Press 0 to add or edit your league name. ")
    print("Press 1 to add a new team. ")
    print("Press 2 to delete an existing team. ")
    print("Press 3 to display current teams in your league. ")
    print("Press 5 to move on to division assignment. ")
    print("TESTS: Press 6 to use the 8-team template. ")
    print("TESTS: Press 7 to use the 16-team template. ")
    print("Press q to quit the program. ")  TODO: add a quit function AS 'q' is not working as designed.
    prompt = input("What would you like to do? ")
    if prompt == "0": # change league name
        for element in league_name: # loop through the list
            league_name.remove(element) # remove all elements in the list
        l_name_l = input("Enter your league name: ") # get the new league name
        l_name = l_name_l + " League"   # add "League" to the end of the new league name
        league_name.append(l_name) # add the new league name to the list
        print("Successfully changed your league name to {}. ".format(l_name)) # print the new league name
        kg = input("Press any key to return to main menu... ") TODO: you must press the <enter> key to continue! Fix this.
        if kg == "0": # if the user presses 0
            main() # go back to the main menu
        else:
            main() # go back to the main menu
    elif prompt == "1": # add a new team
        print("") 
        print("You can enter multiple teams. Separate them with a space.")
        new_team = input("Enter a team name here to add it to your league: ") TODO: get a list of teams from csv/xlsx file.
        temp_teams = new_team.split(" ") # split the new team by space
        for te in temp_teams: # for each team
            teams.append(te) # add the team to the teams list
        print("Successfully added the {} to your league. ".format(new_team)) # print the new team
        kg = input("Press any key to return to main menu... ")
        if kg == "0": # if the user presses 0
            main() # go back to the main menu
        else:
            main() # go back to the main menu
    elif prompt == "2": # delete a team
        print("")
        to_delete = input("Enter team to delete: ") # get the team to delete
        if to_delete in teams: # if the team is in the teams list
            teams.remove(to_delete) # remove the team from the teams list
            print("Deleted " + to_delete + " from the list.") # print the deleted team
        else:
            print("Team not found in list. ")
        kg = input("Press any key to return to main menu... ")
        if kg == "0": # if the user presses 0
            main() # go back to the main menu
        else:
            main() # go back to the main menu
    elif prompt == "3": # display current teams
        print("")
        print("Current Team Members: ")
        for team in teams: # for each team
            print(" -  {}".format(team)) # print the team
        print("")
        kg = input("Press any key to return to main menu... ")
        if kg == "0": # if the user presses 0
            main() # go back to the main menu
        else:
            main() # go back to the main menu
    elif prompt == "5": # move on to division assignment
        if len(teams) < 4: # if there are less than 4 teams
            print("Not enough teams are in your league. Minimum: 4 teams. ")
            print("Add more teams to your league before continuing. ")
            main() # go back to the main menu
        elif len(teams) < 16: # if there are less than 16 teams
            assign_division_8() # assign the teams to divisions
        elif len(teams) >= 16: # if there are 16 or more teams
            assign_division_16() # assign the teams to divisions
        elif len(teams) > 100: # if there are more than 100 teams
            print("The maximum number of teams is 100. Delete some teams from your list before continuing. ")
            main() # go back to the main menu
        else:
            print("You appear to have too little or too many teams in your league. Please check your teams again. ")
            main() # go back to the main menu
    elif prompt == "6": # use the 8-team template
        # Remove any current teams in the TEAMS list
        for team in teams: # for each team
            teams.remove(team) # remove the team
        # Add all items from test_8 into the TEAMS list
        for team in test_8: # for each team in the test_8 list    
            teams.append(team) # add the team to the teams list
        print("Teams: ") # print the teams
        print(teams) # print the teams
        assign_division_8() # assign the teams to divisions
    elif prompt == "7": # use the 16-team template
        for team in teams: # for each team
            teams.remove(team) # remove the team
        for team in test_16: # for each team in the test_16 list
            teams.append(team) # add the team to the teams list
        print("Teams: ")    
        print(teams) # print the teams
        assign_division_16() # assign the teams to divisions
    else:
        print("Invalid argument entered. ")
        main() # go back to the main menu


def assign_division_16(): # assign the teams to divisions
    print("")
    div = input("How many divisions will be in your league? Select 0, 2, or 4: ") # get the number of divisions

    if div == "0": # if there are 0 divisions
        create_schedule() # create the schedule
        print(div + " divisions selected for your league. ")
    elif div == "2" or "4": # if there are 2 or 4 divisions
        print("How would you like to do division assignment? ")
        print("Press 1 for random assignment. ")
        print("Press 2 for manual assignment")
        res = input(" ") # get the response
        if res == "1" and div == "4": # if the response is 1 and there are 4 divisions
            print("Randomly diving your teams into 4 different divisions....... ")
            sleep(2.5) # sleep for 2.5 seconds
            print("Success!")
            for s in range(0, 4): # for each team
                # div 1
                for x in range(0, 1): # for each team
                    div1.append(teams[random.randint(0, len(teams)-1)]) # add the team to division 1
                for item in div1: # for each item in division 1
                    if item in teams: # if the item is in the teams list
                        teams.remove(item) # remove the item from the teams list
                # div 2
                for y in range(0, 1): # for each team
                    div2.append(teams[random.randint(0, len(teams)-1)]) # add the team to division 2
                for item in div2: # for each item in division 2
                    if item in teams: # if the item is in the teams list
                        teams.remove(item) # remove the item from the teams list
                # div 3
                for z in range(0, 1): # for each team
                    div3.append(teams[random.randint(0, len(teams)-1)]) # add the team to division 3
                for item in div3: # for each item in division 3
                    if item in teams: # if the item is in the teams list
                        teams.remove(item) # remove the item from the teams list
                # div 4
                for q in range(0, 1):  # for each team
                    div4.append(teams[random.randint(0, len(teams)-1)]) # add the team to division 4
                for item in div4: # for each item in division 4
                    if item in teams:   # if the item is in the teams list
                        teams.remove(item) # remove the item from the teams list
            for di in div1:     # for each item in division 1
                teams.append(di)   # add the item to the teams list
            for de in div2:     # for each item in division 2
                teams.append(de)  # add the item to the teams list
            for du in div3:    # for each item in division 3
                teams.append(du) # add the item to the teams list
            for do in div4:   # for each item in division 4
                teams.append(do) # add the item to the teams list
            print("teams = ")
            print(teams)
            print("div 1 = ")
            print(div1)
            print("div 2 = ")
            print(div2)
            print("div 3 = ")
            print(div3)
            print("div 4 = ")
            print(div4)
            move = input("Press any key to continue... ") # TODO: you must press the <enter> key to continue! Fix this.
            if move == "yes": # if the user presses yes
                create_schedule() # create the schedule
            else:
                create_schedule() # create the schedule
        elif res == "1" and div == "2": # if the response is 1 and there are 2 divisions
            print("Randomly diving your teams into 2 different divisions..... ")
            sleep(2.5)  # sleep for 2.5 seconds
            print("Success!")
            for r in range(0,8): 
                # div 1
                for x in range(0, 1): # for each team
                    div1.append(teams[random.randint(0, len(teams) - 1)]) # add the team to division 1
                for item in div1: # for each item in division 1
                    if item in teams: # if the item is in the teams list
                        teams.remove(item) # remove the item from the teams list
                # div 2
                for y in range(0, 1): # for each team
                    div2.append(teams[random.randint(0, len(teams) - 1)]) # add the team to division 2
                for item in div2: # for each item in division 2
                    if item in teams: # if the item is in the teams list
                        teams.remove(item)  # remove the item from the teams list
            for di in div1:     # for each item in division 1
                teams.append(di)    # add the item to the teams list
            for de in div2:    # for each item in division 2
                teams.append(de)  # add the item to the teams list
            print("teams = ")
            print(teams)
            print("div 1 = ")
            print(div1)
            print("div 2 = ")
            print(div2)
            move = input("Press any key to continue... ")  
            if move == "yes": # if the user presses yes
                create_schedule() # create the schedule
            else:
                create_schedule() # create the schedule
        elif res == "2": # if the response is 2
            manual_assign(teams, div) # manually assign the teams to divisions
    else:
        print("Please enter a valid option. 0, 2 or 4. ")
        assign_division_8() # assign the teams to divisions


def assign_division_8():
    print("you reached assign division two function") # assign the teams to divisions
    if len(teams) < 16: # if there are less than 16 teams
        print("")
        print("NOTE: You currently have less than 16 teams in your league. ")
        print("You can only choose 0 or 2 divisions. ")
        div = input("How many divisions will be in your league? Select 0 or 2: ") # get the number of divisions
        if div == "0": # if there are 0 divisions
            create_schedule() # create the schedule
            print(div + " divisions selected for your league. ")
        elif div == "2": # if there are 2 divisions
            print("How would you like to do division assignment? ")
            print("Press 1 for random assignment. ")
            print("Press 2 for manual assignment")
            res = input("") # get the response
            if res == "1": # if the response is 1
                print("Randomly diving your teams into 2 different divisions..... ")
                sleep(2.5) # sleep for 2.5 seconds
                print("Success!")
                for r in range(0,4): # for each team
                    for x in range(0, 1):   # for each team
                        div1.append(teams[random.randint(0, len(teams) - 1)])   # add the team to division 1
                    for item in div1:   # for each item in division 1
                        if item in teams:  # if the item is in the teams list
                            teams.remove(item)  # remove the item from the teams list
                    # div 2
                    for y in range(0, 1):   # for each team
                        div2.append(teams[random.randint(0, len(teams) - 1)])  # add the team to division 2
                    for item in div2: # for each item in division 2
                        if item in teams: # if the item is in the teams list
                            teams.remove(item) # remove the item from the teams list
                for di in div1: # for each item in division 1
                    teams.append(di) # add the item to the teams list
                for de in div2: # for each item in division 2
                    teams.append(de) # add the item to the teams list
                print("teams = ")
                print(teams) # print the teams
                print("div 1 = ")
                print(div1)     # print division 1
                print("div 2 = ")
                print(div2)    # print division 2
                move = input("Press any key to continue... ")
                if move == "yes": # if the user presses yes
                    create_schedule() # create the schedule
                else:
                    create_schedule() # create the schedule
            elif res == "2":    # if the response is 2
                divisions_number = int(div) # get the number of divisions
                manual_assign(teams, divisions_number) # manually assign the teams to divisions
        else:
            print("Please enter a valid option. 0 or 2. ") # print an error message
            assign_division_16() # assign the teams to divisions


def manual_assign(array, no_divisions): # manually assign the teams to divisions
    if len(div1) <= 1:   # if there is 1 or less team in division 1
        for a in array: # for each team in the array
            remaining.append(a) # add the team to the remaining list
    if len(array) < 16: # if there are less than 16 teams
        div = int(no_divisions) # get the number of divisions
        if div == 2: # if there are 2 divisions
            print(" ")
            print("Remaining Teams needed to be assigned: ")
            for r in remaining: # for each team in the remaining list
                print(r)
            print(" ")
            print("Press 1 to add a team(s) to division 1. ")
            print("Press 2 to add a team(s) to division 2. ")
            print("Press 3 to see your current divisions and teams")
            print("Press 4 to return to random assignment. ")
            print("Press 5 to create your schedule! ")
            answer = input("What would you like to do? ") 
            if answer == "1": # if the answer is 1
                print("You can enter multiple teams. Separate them with a space.")
                t1 = input("Enter team to add to division 1: ") # get the team to add to division 1
                temp_teams = t1.split(" ") # split the team by space
                for team in temp_teams: # for each team
                    if team in array: # if the team is in the array
                        div1.append(team) # add the team to division 1
                        remaining.remove(team) # remove the team from the remaining list
                        print("Added {} to division 1. ".format(team)) # print the added team
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team)) # print an error message
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            elif answer == "2":     # if the answer is 2
                print("You can enter multiple teams. Separate them with a space.")
                t2 = input("Enter team to add to division 2: ") # get the team to add to division 2
                temp_teams = t2.split(" ") # split the team by space
                for team in temp_teams: # for each team
                    if team in array: # if the team is in the array
                        div2.append(team)   # add the team to division 2
                        remaining.remove(team) # remove the team from the remaining list
                        print("Added {} to division 2. ".format(team)) # print the added team
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team)) TODO: when selecting a team NOT in array, the Remaining Teams needed to be assigned list is duplicated. Fix this.
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            elif answer == "3": # if the answer is 3
                print(" ")
                print("DIVISION 1:")    # print division 1
                for times in div1: # for each team in division 1
                    print(times) # print the team
                print(" ")
                print("DIVISION 2:")   # print division 2
                for times in div2: # for each team in division 2
                    print(times) # print the team
                print(" ")
                manual_assign(array, no_divisions) # manually assign the teams to divisions 
            elif answer == "4": # if the answer is 4
                for i in div1: # for each team in division 1
                    div1.remove(i) # remove the team from division 1
                for i in div2: # for each team in division 2
                    div2.remove(i) # remove the team from division 2
                assign_division_8() # assign the teams to divisions
            elif answer == "5": # if the answer is 5
                create_schedule()   # create the schedule
            else:
                manual_assign(array, no_divisions) # manually assign the teams to divisions
    elif len(array) >= 16: # if there are 16 or more teams
        div = int(no_divisions)     # get the number of divisions
        if div == 2: # if there are 2 divisions
            print(" ")
            print("Here are the current teams in your league: ")
            for a in array: # for each team in the array
                print(a) # print the team
            print(" ")
            print("Press 1 to add a team(s) to division 1. ")
            print("Press 2 to add a team(s) to division 2. ")
            print("Press 3 to see your current divisions and teams")
            print("Press 4 to return to random assignment. ")
            print("Press 5 to create your schedule! ")
            answer = input("What would you like to do? ")
            if answer == "1": # if the answer is 1
                print("You can enter multiple teams. Separate them with a space.")
                t1 = input("Enter team to add to division 1: ") # get the team to add to division 1
                temp_teams = t1.split(" ") # split the team by space
                for team in temp_teams: # for each team
                    if team in array: # if the team is in the array
                        div1.append(team) # add the team to division 1
                        remaining.remove(team) # remove the team from the remaining list
                        print("Added {} to division 1. ".format(team)) # print the added team
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team)) # print an error message
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            elif answer == "2": # if the answer is 2
                print("You can enter multiple teams. Separate them with a space.")
                t2 = input("Enter team to add to division 2: ")
                temp_teams = t2.split(" ") # split the team by space
                for team in temp_teams: # for each team
                    if team in array: # if the team is in the array
                        div2.append(team) # add the team to division 2
                        remaining.remove(team) # remove the team from the remaining list
                        print("Added {} to division 2. ".format(team)) # print the added team
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team)) # print an error message
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            elif answer == "3": # if the answer is 3
                print(" ")
                print("DIVISION 1:") # print division 1
                for times in div1: # for each team in division 1
                    print(times) # print the team
                print(" ")
                print("DIVISION 2:") # print division 2
                for times in div2: # for each team in division 2
                    print(times) # print the team
                print(" ")
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            elif answer == "4": # if the answer is 4
                for i in div1: # for each team in division 1
                    div1.remove(i) # remove the team from division 1
                for i in div2: # for each team in division 2
                    div2.remove(i) # remove the team from division 2
                assign_division_8() # assign the teams to divisions
            elif answer == "5": # if the answer is 5
                create_schedule() # create the schedule
            else:
                manual_assign(array, no_divisions) # manually assign the teams to divisions
        elif div == 4:  # if there are 4 divisions
            print(" ")
            print("Here are the current teams in your league: ")
            for a in array:     # for each team in the array
                print(a) # print the team
            print(" ")
            print("Press 1 to add a team(s) to division 1. ")
            print("Press 2 to add a team(s) to division 2. ")
            print("Press 3 to add a team(s) to division 3. ")
            print("Press 4 to add a team(s) to division 3. ")
            print("Press 5 to see your current divisions and teams")
            print("Press 6 to return to random assignment. ")
            print("Press 7 to create your schedule! ")
            answer = input("What would you like to do? ")
            if answer == "1": # if the answer is 1
                print("You can enter multiple teams. Separate them with a space.")
                t1 = input("Enter team to add to division 1: ") # get the team to add to division 1
                temp_teams = t1.split(" ") # split the team by space
                for team in temp_teams: # for each team
                    if team in array: # if the team is in the array
                        div1.append(team) # add the team to division 1
                        remaining.remove(team) # remove the team from the remaining list
                        print("Added {} to division 1. ".format(team)) # print the added team
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team)) # print an error message
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            elif answer == "2": # if the answer is 2
                print("You can enter multiple teams. Separate them with a space.")
                t2 = input("Enter team to add to division 2: ") # get the team to add to division 2
                temp_teams = t2.split(" ") # split the team by space
                for team in temp_teams: # for each team
                    if team in array: # if the team is in the array
                        div2.append(team) # add the team to division 2
                        remaining.remove(team) # remove the team from the remaining list
                        print("Added {} to division 2. ".format(team)) # print the added team
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team)) # print an error message
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            if answer == "3": # if the answer is 3
                print("You can enter multiple teams. Separate them with a space.")
                t3 = input("Enter team to add to division 3: ") # get the team to add to division 3
                temp_teams = t3.split(" ") # split the team by space
                for team in temp_teams: # for each team
                    if team in array: # if the team is in the array
                        div3.append(team) # add the team to division 3
                        remaining.remove(team) # remove the team from the remaining list
                        print("Added {} to division 3. ".format(team)) # print the added team
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team)) # print an error message
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            elif answer == "4": # if the answer is 4
                print("You can enter multiple teams. Separate them with a space.") 
                t4 = input("Enter team to add to division 4: ") # get the team to add to division 4
                temp_teams = t4.split(" ") # split the team by space
                for team in temp_teams: # for each team   
                    if team in array: # if the team is in the array
                        div4.append(team) # add the team to division 4
                        remaining.remove(team) # remove the team from the remaining list
                        print("Added {} to division 4. ".format(team)) # print the added team
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team)) # print an error message
                manual_assign(array, no_divisions) # manually assign the teams to divisions
            elif answer == "5": # if the answer is 5
                print(" ")
                print("DIVISION 1:") # print division 1
                for times in div1: # for each team in division 1
                    print(times) # print the team
                print("DIVISION 2:") # print division 2
                for times in div2: # for each team in division 2
                    print(times) # print the team
                print("DIVISION 3:") # print division 3
                for times in div3: # for each team in division 3
                    print(times) # print the team
                print("DIVISION 4:") # print division 4
                for times in div4: # for each team in division 4
                    print(times) # print the team
                print(" ")
                manual_assign(array, no_divisions)  # manually assign the teams to divisions
            elif answer == "6": # if the answer is 6
                for i in div1: # for each team in division 1
                    div1.remove(i) # remove the team from division 1
                for i in div2: # for each team in division 2
                    div2.remove(i) # remove the team from division 2
                assign_division_8() # assign the teams to divisions
            elif answer == "7": # if the answer is 7
                create_schedule() # create the schedule
            else:
                manual_assign(array, no_divisions) # manually assign the teams to divisions
    else:
        manual_assign(array, no_divisions) # manually assign the teams to divisions


def create_schedule(): # create the schedule
    while True: # while true
        print(" ") # print a space
        weeks = input("Enter the amount of rounds(weeks) you want in your league tournament: ")
        if weeks.isdigit():     # if the input is a digit
            weeks_1 = int(weeks) # get the number of weeks
            if weeks_1 == 0: # if the number of weeks is 0
                print("A league must have more than 0 weeks. Please enter a number greater than 0. ")
                create_schedule() # create the schedule
            elif weeks_1 >= 100: # if the number of weeks is greater than or equal to 100
                print("Consider shortening the amount of weeks. ")
                anq = input("Enter 0 to pick another number or press any other key to continue. ")
                if anq == '0': # if the user enters 0
                    create_schedule()    # create the schedule
                else:
                    print(" ")
                    print("Now generating your complete schedule with a total of {} rounds.... ".format(weeks))
                    sleep(float(weeks) - (float(weeks) / 2)) # sleep for half the number of weeks
                    # Put each team in the teams array into its own array
                    plan = round_robin(teams, int(weeks)) # create the schedule
                    counted = 1 # set the count to 1
                    print(" ")
                    print("{} FULL {} WEEK SCHEDULE! ".format(league_name[0], weeks)) # print the league name and number of weeks
                    print(" ")
                    print("MATCHUPS:")
                    for pl in plan: # for each plan
                        # print(" Week {} - {}".format(counted, pl)) # print the week and plan
                        print("Week {}".format(counted)) # print the week
                        for pi in pl: # for each plan item
                            print("  {} vs {}".format(pi[0], pi[1])) # print the matchup
                        counted = counted + 1 # increment the count
                    break
            else:
                print(" ")
                print("Now generating your complete schedule with a total of {} rounds.... ".format(weeks)) # print the number of weeks
                sleep(float(weeks)-(float(weeks)/2)) # sleep for half the number of weeks
                # Put each team in the teams array into its own array
                plan = round_robin(teams, int(weeks)) # create the schedule
                counted = 1 # set the count to 1
                print(" ")
                print("{} FULL {} WEEK SCHEDULE! ".format(league_name[0], weeks)) # print the league name and number of weeks
                print(" ")
                print("MATCHUPS:") # print matchups
                for pl in plan: # for each plan
                    # print(" Week {} - {}".format(counted, pl))
                    print("Week {}".format(counted)) # print the week
                    for pi in pl: # for each plan item
                        print("  {} vs {}".format(pi[0], pi[1])) # print the matchup
                    counted = counted + 1 # increment the count
                break 
        else:
            print("Error. Please enter a number.")
            create_schedule()
    # if len(teams) < 16:
    #     for team in teams:
    #         print("")
    #         team_specific_schedule = [team]
    #         print(team_specific_schedule)
    # else:
    #     for team in teams:
    #         team_specific_schedule = [team]
    #         print("")
    #         print(team_specific_schedule)
            # add_info(team_specific_schedule)
            # remove_self_name(team_specific_schedule)




# def add_info(obj):
#     for t in teams:
#         obj.append(t)
#     print("Before: ")
#     print(obj)
#
#
# def remove_self_name(obj):
#     for ele in obj:
#         if ele == obj[0]:
#             obj.remove(ele)
#     print("After: ")
#     print(obj)


print("")
print("Welcome to your sport schedule and league auto-creator!")

main()