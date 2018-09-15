import pygal
from die import Die

die_roll = Die()

results = []

for i in range(1000000):
  rolls = die_roll.roll()
  results.append(rolls)

total = []
for j in range(1, die_roll.num_of_sides + 1):
  die_side = results.count(j)
  total.append(die_side)

hist = pygal.Bar()
hist.title = "Results of rolling a Die 1,000,000 times."
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Die Sides"
hist.y_title = "Results"
hist.add("Die", total)
hist.render_to_file("die_roll_total.svg")
