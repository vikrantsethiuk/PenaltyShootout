from random import randint
from termcolor import colored,cprint

def display_score():
  print(colored("━" * len(team_1)*5,'blue'))
  for i in range(len(team_1)):
    print(colored(team_1[i],'magenta'), end = '   ')
  print("\n")
  

  for i in range(len(team_2)):
    print(colored(team_2[i],'yellow'), end = '   ') 
  print("")
  print(colored("━" * len(team_1)*5,'blue'))
  print("\n")


def display_legend():
  cprint("1 = Top Left      ", "red",'on_green')
  cprint("2 = Bottom Left   ", "green",'on_red')
  cprint("3 = Top Right     ", "red",'on_green')
  cprint("4 = Bottom Right  ", "green",'on_red')
  cprint("5 = Middle        ", "red",'on_green')
  cprint("\n")

def validate_goal(shoot_pos):

  goal_pos= randint(1,5)

  if shoot_pos != goal_pos and shoot_pos <=5:
    print(colored("Amazing shot, It's a goal\n", "green"))
    return goal
  elif team1_shoot > 5:
    print(colored("Complete miss - Not even on target\n", "red"))
  else:
    print(colored("Unlucky - Good shot though\n", "red"))

  return miss
 
def display_result(team1_goals,team2_goals):

  print("Final Score ")
  print("Team 1 - ", team1_goals)
  print("Team 2 - ", team2_goals)

  if team1_goals> team2_goals:
    print("Team 1 WINS ")
  elif team1_goals == team2_goals:
    print("TIE")
  else:
    print("Team 2 WINS")


   

# Start of the Main Program

team_1 = ["Team 1","-","-","-","-","-"]
team_2 = ["Team 2","-","-","-","-","-"]

team1_goals = 0
team2_goals = 0

goal = "✓"
miss = "X"

counter = 1

display_legend()

while counter <=5 or (team1_goals == team2_goals and counter >5):
  
  if counter>5:
      print(colored("===SUDDEN DEATH===",'red'))

  print(colored("-----Team 1-----", "magenta"))
  team1_shoot = int(input("Enter a number from 1 to 5 where you are going to shoot : "))

  if validate_goal(team1_shoot) == goal:  
    team1_goals += 1
    if counter>5:
      team_1.append(goal)
    else:
      team_1[counter] = goal
  else:
    if counter>5:
      team_1.append(miss)
    else:
      team_1[counter] = miss


  print(colored("-----Team 2-----", "yellow"))
  team2_shoot = int(input("Enter a number from 1 to 5 where you are going to shoot : "))
  if validate_goal(team2_shoot) == goal:
    team2_goals += 1
    if counter>5:
      team_2.append(goal)
    else:
      team_2[counter] = goal
  else:
    if counter>5:
      team_2.append(miss)
    else:
      team_2[counter] = miss

  display_score()
  counter += 1

display_result(team1_goals,team2_goals)



















# computer_number = randint(1,5)


# for i in range(5):
#   where_shoot = int(input("Enter a number from 1 to five where you are going to shoot : "))

#   if computer_number == where_shoot:
#     opposing_score = opposing_score + 1 
#     print("Unlucky")
#     print("Good shot though")

#   elif where_shoot > 5:
#     opposing_score = opposing_score + 1  
#     print("Complete miss")

#   else:
#     print("Amazing shot, It's a goal")
#     your_team = your_team + 1

# print(str(your_team) + "-" + str(opposing_score))
