import random
from time import sleep

test_8 = ["Jets", "Hawks", "Coyotes", "Leopards", "Lions", "Warriors", "Mules", "Lunas"]
test_16 = ["Jets", "Hawks", "Coyotes", "Leopards", "Lions", "Warriors", "Mules", "Lunas",
           "Falcons", "Menehunes", "Koa", "Raiders", "Gladiators", "Tigers", "Sharks", "Bulls"]
league_name = ['My League']
games = 16

teams = []
div1 = []
div2 = []
div3 = []
div4 = []

remaining = []

# subprocess.call(["afplay", "high_hat.wav"])

# d = {'Patriots' : 'Brady', 'Chiefs' : 'Mahomes', 'Warriors' : 'Curry'}
# while d:
#     key, value = d.popitem()
#     print(key, '-->', value)


def round_robin(teamshere, rounds):
    # bye
    if len(teamshere) % 2:
        teamshere.append(None)

    schedule = []
    for tor in range(rounds):
        matchups = []
        length = len(teamshere)
        for i in range(int(length / 2)):
            pairing = (teamshere[i], teamshere[len(teamshere) - i - 1])
            # alternate first team
            if i == 0 and tor % 2:
                pairing = pairing[::-1]
            # alternate based on the team's previous round appearance
            if schedule and None not in pairing:
                previous_round = list(sum(schedule[-1], ()))
                for team in pairing:
                    if team in previous_round and pairing[previous_round.index(team) % 2] == team:
                        pairing = pairing[::-1]
            matchups.append(pairing)
        teamshere.insert(1, teamshere.pop())
        schedule.append(matchups)

    return schedule

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
    print("Current League Name: " + ', '.join(league_name) + "\n")
    print("CURRENT OPTIONS: ")
    print("_________________________")
    print("Press 0 to add or edit your league name. ")
    print("Press 1 to add a new team. ")
    print("Press 2 to delete an existing team. ")
    print("Press 3 to display current teams in your league. ")
    print("Press 5 to move on to division assignment. ")
    print("TESTS: Press 6 to use the 8-team template. ")
    print("TESTS: Press 7 to use the 16-team template. ")
    print("Press q to quit the program. ")
    prompt = input("What would you like to do? ")
    if prompt == "0":
        for element in league_name:
            league_name.remove(element)
        l_name_l = input("Enter your league name: ")
        l_name = l_name_l
        league_name.append(l_name)
        print("Successfully changed your league name to {}. ".format(l_name))
        kg = input("Press any key to return to main menu... ")
        if kg == "0":
            main()
        else:
            main()
    elif prompt == "1":
        print("")
        print("You can enter multiple teams. Separate them with a space.")
        new_team = input("Enter a team name here to add it to your league: ")
        temp_teams = new_team.split(" ")
        for te in temp_teams:
            teams.append(te)
        print("Successfully added the {} to your league. ".format(new_team))
        kg = input("Press any key to return to main menu... ")
        if kg == "0":
            main()
        else:
            main()
    elif prompt == "2":
        print("")
        to_delete = input("Enter team to delete: ")
        if to_delete in teams:
            teams.remove(to_delete)
            print("Deleted " + to_delete + " from the list.")
        else:
            print("Team not found in list. ")
        kg = input("Press any key to return to main menu... ")
        if kg == "0":
            main()
        else:
            main()
    elif prompt == "3":
        print("")
        print("Current Team Members: ")
        for team in teams:
            print(" -  {}".format(team))
        print("")
        kg = input("Press any key to return to main menu... ")
        if kg == "0":
            main()
        else:
            main()
    elif prompt == "5":
        if len(teams) < 4:
            print("Not enough teams are in your league. Minimum: 4 teams. ")
            print("Add more teams to your league before continuing. ")
            main()
        elif len(teams) < 16:
            assign_division_8()
        elif len(teams) >= 16:
            assign_division_16()
        elif len(teams) > 100:
            print("The maximum number of teams is 100. Delete some teams from your list before continuing. ")
            main()
        else:
            print("You appear to have too little or too many teams in your league. Please check your teams again. ")
            main()
    elif prompt == "6":
        # Remove any current teams in the TEAMS list
        for team in teams:
            teams.remove(team)
        # Add all items from test_8 into the TEAMS list
        for team in test_8:
            teams.append(team)
        print("Teams: ")
        print(teams)
        assign_division_8()
    elif prompt == "7":
        for team in teams:
            teams.remove(team)
        for team in test_16:
            teams.append(team)
        print("Teams: ")
        print(teams)
        assign_division_16()
    else:
        print("Invalid argument entered. ")
        main()


def assign_division_16():
    print("")
    div = input("How many divisions will be in your league? Select 0, 2, or 4: ")

    if div == "0":
        create_schedule()
        print(div + " divisions selected for your league. ")
    elif div == "2" or "4":
        print("How would you like to do division assignment? ")
        print("Press 1 for random assignment. ")
        print("Press 2 for manual assignment")
        res = input(" ")
        if res == "1" and div == "4":
            print("Randomly diving your teams into 4 different divisions....... ")
            sleep(2.5)
            print("Success!")
            for s in range(0, 4):
                # div 1
                for x in range(0, 1):
                    div1.append(teams[random.randint(0, len(teams)-1)])
                for item in div1:
                    if item in teams:
                        teams.remove(item)
                # div 2
                for y in range(0, 1):
                    div2.append(teams[random.randint(0, len(teams)-1)])
                for item in div2:
                    if item in teams:
                        teams.remove(item)
                # div 3
                for z in range(0, 1):
                    div3.append(teams[random.randint(0, len(teams)-1)])
                for item in div3:
                    if item in teams:
                        teams.remove(item)
                # div 4
                for q in range(0, 1):
                    div4.append(teams[random.randint(0, len(teams)-1)])
                for item in div4:
                    if item in teams:
                        teams.remove(item)
            for di in div1:
                teams.append(di)
            for de in div2:
                teams.append(de)
            for du in div3:
                teams.append(du)
            for do in div4:
                teams.append(do)
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
            move = input("Press any key to continue... ")
            if move == "yes":
                create_schedule()
            else:
                create_schedule()
        elif res == "1" and div == "2":
            print("Randomly diving your teams into 2 different divisions..... ")
            sleep(2.5)
            print("Success!")
            for r in range(0,8):
                # div 1
                for x in range(0, 1):
                    div1.append(teams[random.randint(0, len(teams) - 1)])
                for item in div1:
                    if item in teams:
                        teams.remove(item)
                # div 2
                for y in range(0, 1):
                    div2.append(teams[random.randint(0, len(teams) - 1)])
                for item in div2:
                    if item in teams:
                        teams.remove(item)
            for di in div1:
                teams.append(di)
            for de in div2:
                teams.append(de)
            print("teams = ")
            print(teams)
            print("div 1 = ")
            print(div1)
            print("div 2 = ")
            print(div2)
            move = input("Press any key to continue... ")
            if move == "yes":
                create_schedule()
            else:
                create_schedule()
        elif res == "2":
            manual_assign(teams, div)
    else:
        print("Please enter a valid option. 0, 2 or 4. ")
        assign_division_8()


def assign_division_8():
    print("you reached assign division two function")
    if len(teams) < 16:
        print("")
        print("NOTE: You currently have less than 16 teams in your league. ")
        print("You can only choose 0 or 2 divisions. ")
        div = input("How many divisions will be in your league? Select 0 or 2: ")
        if div == "0":
            create_schedule()
            print(div + " divisions selected for your league. ")
        elif div == "2":
            print("How would you like to do division assignment? ")
            print("Press 1 for random assignment. ")
            print("Press 2 for manual assignment")
            res = input("")
            if res == "1":
                print("Randomly diving your teams into 2 different divisions..... ")
                sleep(2.5)
                print("Success!")
                for r in range(0,4):
                    for x in range(0, 1):
                        div1.append(teams[random.randint(0, len(teams) - 1)])
                    for item in div1:
                        if item in teams:
                            teams.remove(item)
                    # div 2
                    for y in range(0, 1):
                        div2.append(teams[random.randint(0, len(teams) - 1)])
                    for item in div2:
                        if item in teams:
                            teams.remove(item)
                for di in div1:
                    teams.append(di)
                for de in div2:
                    teams.append(de)
                print("teams = ")
                print(teams)
                print("div 1 = ")
                print(div1)
                print("div 2 = ")
                print(div2)
                move = input("Press any key to continue... ")
                if move == "yes":
                    create_schedule()
                else:
                    create_schedule()
            elif res == "2":
                divisions_number = int(div)
                manual_assign(teams, divisions_number)
        else:
            print("Please enter a valid option. 0 or 2. ")
            assign_division_16()


def manual_assign(array, no_divisions):
    if len(div1) <= 1:
        for a in array:
            remaining.append(a)
    if len(array) < 16:
        div = int(no_divisions)
        if div == 2:
            print(" ")
            print("Remaining Teams needed to be assigned: ")
            for r in remaining:
                print(r)
            print(" ")
            print("Press 1 to add a team(s) to division 1. ")
            print("Press 2 to add a team(s) to division 2. ")
            print("Press 3 to see your current divisions and teams")
            print("Press 4 to return to random assignment. ")
            print("Press 5 to create your schedule! ")
            answer = input("What would you like to do? ")
            if answer == "1":
                print("You can enter multiple teams. Separate them with a space.")
                t1 = input("Enter team to add to division 1: ")
                temp_teams = t1.split(" ")
                for team in temp_teams:
                    if team in array:
                        div1.append(team)
                        remaining.remove(team)
                        print("Added {} to division 1. ".format(team))
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team))
                manual_assign(array, no_divisions)
            elif answer == "2":
                print("You can enter multiple teams. Separate them with a space.")
                t2 = input("Enter team to add to division 2: ")
                temp_teams = t2.split(" ")
                for team in temp_teams:
                    if team in array:
                        div2.append(team)
                        remaining.remove(team)
                        print("Added {} to division 2. ".format(team))
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team))
                manual_assign(array, no_divisions)
            elif answer == "3":
                print(" ")
                print("DIVISION 1:")
                for times in div1:
                    print(times)
                print(" ")
                print("DIVISION 2:")
                for times in div2:
                    print(times)
                print(" ")
                manual_assign(array, no_divisions)
            elif answer == "4":
                for i in div1:
                    div1.remove(i)
                for i in div2:
                    div2.remove(i)
                assign_division_8()
            elif answer == "5":
                create_schedule()
            else:
                manual_assign(array, no_divisions)
    elif len(array) >= 16:
        div = int(no_divisions)
        if div == 2:
            print(" ")
            print("Here are the current teams in your league: ")
            for a in array:
                print(a)
            print(" ")
            print("Press 1 to add a team(s) to division 1. ")
            print("Press 2 to add a team(s) to division 2. ")
            print("Press 3 to see your current divisions and teams")
            print("Press 4 to return to random assignment. ")
            print("Press 5 to create your schedule! ")
            answer = input("What would you like to do? ")
            if answer == "1":
                print("You can enter multiple teams. Separate them with a space.")
                t1 = input("Enter team to add to division 1: ")
                temp_teams = t1.split(" ")
                for team in temp_teams:
                    if team in array:
                        div1.append(team)
                        remaining.remove(team)
                        print("Added {} to division 1. ".format(team))
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team))
                manual_assign(array, no_divisions)
            elif answer == "2":
                print("You can enter multiple teams. Separate them with a space.")
                t2 = input("Enter team to add to division 2: ")
                temp_teams = t2.split(" ")
                for team in temp_teams:
                    if team in array:
                        div2.append(team)
                        remaining.remove(team)
                        print("Added {} to division 2. ".format(team))
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team))
                manual_assign(array, no_divisions)
            elif answer == "3":
                print(" ")
                print("DIVISION 1:")
                for times in div1:
                    print(times)
                print(" ")
                print("DIVISION 2:")
                for times in div2:
                    print(times)
                print(" ")
                manual_assign(array, no_divisions)
            elif answer == "4":
                for i in div1:
                    div1.remove(i)
                for i in div2:
                    div2.remove(i)
                assign_division_8()
            elif answer == "5":
                create_schedule()
            else:
                manual_assign(array, no_divisions)
        elif div == 4:
            print(" ")
            print("Here are the current teams in your league: ")
            for a in array:
                print(a)
            print(" ")
            print("Press 1 to add a team(s) to division 1. ")
            print("Press 2 to add a team(s) to division 2. ")
            print("Press 3 to add a team(s) to division 3. ")
            print("Press 4 to add a team(s) to division 3. ")
            print("Press 5 to see your current divisions and teams")
            print("Press 6 to return to random assignment. ")
            print("Press 7 to create your schedule! ")
            answer = input("What would you like to do? ")
            if answer == "1":
                print("You can enter multiple teams. Separate them with a space.")
                t1 = input("Enter team to add to division 1: ")
                temp_teams = t1.split(" ")
                for team in temp_teams:
                    if team in array:
                        div1.append(team)
                        remaining.remove(team)
                        print("Added {} to division 1. ".format(team))
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team))
                manual_assign(array, no_divisions)
            elif answer == "2":
                print("You can enter multiple teams. Separate them with a space.")
                t2 = input("Enter team to add to division 2: ")
                temp_teams = t2.split(" ")
                for team in temp_teams:
                    if team in array:
                        div2.append(team)
                        remaining.remove(team)
                        print("Added {} to division 2. ".format(team))
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team))
                manual_assign(array, no_divisions)
            if answer == "3":
                print("You can enter multiple teams. Separate them with a space.")
                t3 = input("Enter team to add to division 3: ")
                temp_teams = t3.split(" ")
                for team in temp_teams:
                    if team in array:
                        div3.append(team)
                        remaining.remove(team)
                        print("Added {} to division 3. ".format(team))
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team))
                manual_assign(array, no_divisions)
            elif answer == "4":
                print("You can enter multiple teams. Separate them with a space.")
                t4 = input("Enter team to add to division 4: ")
                temp_teams = t4.split(" ")
                for team in temp_teams:
                    if team in array:
                        div4.append(team)
                        remaining.remove(team)
                        print("Added {} to division 4. ".format(team))
                    else:
                        print("Could not add {}. Team not currently in your league. ".format(team))
                manual_assign(array, no_divisions)
            elif answer == "5":
                print(" ")
                print("DIVISION 1:")
                for times in div1:
                    print(times)
                print("DIVISION 2:")
                for times in div2:
                    print(times)
                print("DIVISION 3:")
                for times in div3:
                    print(times)
                print("DIVISION 4:")
                for times in div4:
                    print(times)
                print(" ")
                manual_assign(array, no_divisions)
            elif answer == "6":
                for i in div1:
                    div1.remove(i)
                for i in div2:
                    div2.remove(i)
                assign_division_8()
            elif answer == "7":
                create_schedule()
            else:
                manual_assign(array, no_divisions)
    else:
        manual_assign(array, no_divisions)


def create_schedule():
    while True:
        print(" ")
        weeks = input("Enter the amount of rounds(weeks) you want in your league tournament: ")
        if weeks.isdigit():
            weeks_1 = int(weeks)
            if weeks_1 == 0:
                print("A league must have more than 0 weeks. Please enter a number greater than 0. ")
                create_schedule()
            elif weeks_1 >= 100:
                print("Consider shortening the amount of weeks. ")
                anq = input("Enter 0 to pick another number or press any other key to continue. ")
                if anq == '0':
                    create_schedule()
                else:
                    print(" ")
                    print("Now generating your complete schedule with a total of {} rounds.... ".format(weeks))
                    sleep(float(weeks) - (float(weeks) / 2))
                    # Put each team in the teams array into its own array
                    plan = round_robin(teams, int(weeks))
                    counted = 1
                    print(" ")
                    print("{} FULL {} WEEK SCHEDULE! ".format(league_name[0], weeks))
                    print(" ")
                    print("MATCHUPS:")
                    for pl in plan:
                        # print(" Week {} - {}".format(counted, pl))
                        print("Week {}".format(counted))
                        for pi in pl:
                            print("  {} vs {}".format(pi[0], pi[1]))
                        counted = counted + 1
                    break
            else:
                print(" ")
                print("Now generating your complete schedule with a total of {} rounds.... ".format(weeks))
                sleep(float(weeks)-(float(weeks)/2))
                # Put each team in the teams array into its own array
                plan = round_robin(teams, int(weeks))
                counted = 1
                print(" ")
                print("{} FULL {} WEEK SCHEDULE! ".format(league_name[0], weeks))
                print(" ")
                print("MATCHUPS:")
                for pl in plan:
                    # print(" Week {} - {}".format(counted, pl))
                    print("Week {}".format(counted))
                    for pi in pl:
                        print("  {} vs {}".format(pi[0], pi[1]))
                    counted = counted + 1
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
