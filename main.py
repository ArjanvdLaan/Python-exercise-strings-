# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
goalScorer1 = "Ruud Gullit"
goalScorer2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = f"{goalScorer1} {goal_0}, {goalScorer2} {goal_1}"
print(scorers)
report = f"{goalScorer1} scored in the {goal_0}nd minute\n{goalScorer2} scored in the {goal_1}th minute"
print(report)

# Part 2
player = "Marco van Basten"
space_index = player.find(" ")
first_name = player[:space_index]
print(first_name)

space_index = player.find(" ")
print(space_index)
last_name = player[space_index + 1:]
last_name_len = len(last_name)
print(last_name_len)

space_index = player.find(" ")
first_initial = player[0]
last_name = player[space_index + 1:]
name_short = f"{first_initial}. {last_name}"
print(name_short)

chant = (f"{first_name}! " * (len(first_name) - 1)) + f"{first_name}!"
print(chant)

good_chant = chant[-1] != " "
print(good_chant)
