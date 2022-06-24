# M2C4 Python Assignment
from decimal import Decimal
import math


# Exercise 1:
my_list = ["red", "orange", "yellow", "green", "blue"]

my_tuple = ("black", "white", "grey")

my_float = 23.48

my_int = 42

my_decimal = Decimal(102.52)

my_dict = {
	"car": "land",
	"boat": "water",
	"plane": "air"
}

# Exercise 2:
my_float_up = math.ceil(my_float)
print(my_float_up)

# Exercise 3:
square_root = math.sqrt(my_float)
print(square_root)

# Exercise 4:
first_ele = list(my_dict.values())[0]
print(first_ele)

# Exercise 5:
second_ele = my_tuple[1]
print(second_ele)

# Exercise 6:
my_list.append("indigo")
print(my_list)

# Exercise 7:
my_list[0] = "crimson"
print(my_list)

# Exercise 8:
sorted_list = sorted(my_list)
print(sorted_list)

# Exercise 9:
new_tuple = list(my_tuple)
new_tuple.append("matter")
my_tuple = tuple(new_tuple)
print(my_tuple)
