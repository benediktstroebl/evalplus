```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize the variables
    min1 = float("inf")
    max1 = float(-inf)
    min2 = float("inf")
    max2 = float(-inf)
    closest1 = min1
    closest2 = min2

    # Compare the first and second numbers in the list
    for num in numbers:
        # Find the smaller number between the first and second
        if num < min1:
            min1 = num
        if num > max1:
            max1 = num
        # Find the smaller number between the first and second
        if num < min2:
            min2 = num
        if num > max2:
            max2 = num

    # Determine the two closest numbers
    if min1 == max1:
        closest1 = min2
    elif min2 == max2:
        closest2 = min1
    else:
        closest1 = min1
        closest2 = max2

    # Return the two closest numbers in the list
    return closest1, closest2
```
This script defines a function called `find_closest_elements`, which takes a list of numbers as an argument and returns a tuple of the two closest numbers in the list. The function uses the approach of iterating over the list, and finding the smaller number between the current number and the smallest of the two closest numbers. The script then compares the numbers and iterates until it finds two numbers that are the closest to each other. It then returns the values of closest pair of numbers.