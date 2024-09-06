```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Input validation
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")

    # Sort the list based on the number
    numbers.sort(numbers, key=lambda num: -num)

    # Initialize variables
    left, right = numbers[0], numbers[-1]
    smallest = left

    # Loop to find the smallest two numbers
    for i in range(1, len(numbers) - 1):
        if numbers[i] < smallest:
            smallest = numbers[i]
        if numbers[i] < left or numbers[i] > right:
            left, right = numbers[i], smallest

    return smallest, right
```
This Python function called find_closest_elements takes a list of numbers as an argument and returns a tuple of the closest pair of numbers. The function first checks if the list contains at least two elements, and raises a ValueError if it doesn't. Then, the list is sorted in ascending order based on the numbers. The function then initializes variables for the leftmost number in the list and the smallest number. Finally, the function loops through the largest number to the left of the list, checking if the current number is smaller than the smallest number. If it is, the smallest number is updated. If the current number is larger than the smallest number or smaller than the right number, the left and right variables are updated with the current number.