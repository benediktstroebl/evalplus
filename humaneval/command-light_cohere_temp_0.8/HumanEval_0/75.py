Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers
    numbers.sort(key=lambda x: (x<threshold or x>threshold))
    # Initialize two boolean lists, one for numbers less than threshold, and one for numbers greater than threshold
    less = [False]
    greater = [False]
    # Loop through the sorted list of numbers
    for num in numbers:
        # If the number is less than the threshold, add it to the list of numbers to check close to
        if num < threshold:
            less.append(True)
        # If the number is greater than the threshold, add it to the list of numbers to check close to
        if num > threshold:
            greater.append(True)
    # If the list of numbers to check close to is empty, return False
        if not(less or greater):
            return False
    # If the list of numbers to check close to is not empty, check if any of the numbers in the list are close to each other
    return any([x and y for x,y in numbers])
```
This function takes a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer than the threshold.

You can use this function to check if any two numbers in a list are closer than a given threshold.