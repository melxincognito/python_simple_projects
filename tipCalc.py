#tip calculator
#need to put float in front of the input so it automatically converts the input to a float
meal = float(input('How much was your meal? '))


tax = 0.0675
tip = 0.15

meal_total = meal + meal * tax
tip_total = meal_total * tip

meal_plus_tip = meal_total + tip_total


print('Your total is: $' + str(meal_plus_tip) +'. You paid $' + str(meal_total) + ' for your meal(tax included) and $' + str(tip_total) + 'for the tip.')


