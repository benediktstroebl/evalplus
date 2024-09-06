Here's the self-contained Python function:
```python
from typing import List
from math import sqrt

def find_closest_elements(numbers: List[float])) -> 

# Returns a tuple containing the two closest numbers in the list, with the smaller number first.
# Input: List[float] numbers
# Initialize a variable to hold the smallest number
smallest = float('inf')

# Initialize a variable to hold the largest number
largest = float('-inf')

# Iterate through the list of numbers
for num in numbers:
    # Calculate the difference between the current number and the current smallest number
    diff = num - smallest
    # Calculate the square of the difference
    diff_squared = diff * diff
    # Check if the difference is less than 0
    if diff_squared < 0:
        smallest = num
        largest = num
    # If the difference is 0, it means we found the minimum and the maximum
    else:
        # Calculate the square root of the difference between the current number and the smallest number
        diff_sqrt = sqrt(diff_squared)
        # Update the largest and smallest numbers
        largest = num
        smallest = diff_sqrt
# Return the two closest numbers
return smallest, largest
```
This Python function, `find_closest_elements`, takes a list of numbers as input and returns a tuple containing the two closest numbers in that list, with the smaller number first. The function initializes two variables, `smallest` and `largest`, to hold the smallest and largest numbers in the list, respectively. It then iterates through each number in the list, calculates the difference between the current number and the smallest number, and if this difference is less than 0, it updates the smallest number to be the current number. Then, it calculates the difference squared and checks if it's less than 0. If it's, it updates the largest number to be the current number and resets the smallest number to be the square root of the difference. The function then continues to iterate through the list until it finds the smallest and largest numbers, at which point it returns them as a tuple.