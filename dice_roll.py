import pygal
from die import Die

first_die = Die()
second_die = Die()

results = []
for i in range(1000000):
  rolls = first_die.roll() + second_die.roll()
  results.append(rolls)

total = []
total_result = first_die.num_of_sides + second_die.num_of_sides
for j in range(2, total_result + 1):
  dice_side = results.count(j)
  total.append(dice_side)

hist = pygal.Bar()
hist.title = "Results of rolling two Dice 1,000,000 times."
hist.x_labels = ["2","3","4","5","6","7","8","9","10","11","12"]
hist.x_title = "Dice Roll Total"
hist.y_title = "Results"
hist.add("Die(1) + Die(2)", total)
hist.render_to_file("dice_roll_total.svg")