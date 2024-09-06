Here is a Python script that contains a self-contained function that solves the problem and passes the test:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Selects two numbers from a supplied list that are the closest to each other and returns them in order (smaller number, larger number).
    Numbers in the list must be floating-point values.
    num1s: List[float]
    closest1: float
    closest2: float
    """
    # Sort the list of numbers
    numbers.sort()

    # Initialize variables to keep track of the closest numbers
    closest1 = numbers[0]
    closest2 = numbers[1]
    # Check if the list has more than two elements
    if len(numbers) > 2:
        # Move the first element to the end of the list
        numbers.append(numbers.pop(0))
        # Rotate the values to sort them numerically
        numbers.sort()
        # Check if the numbers[0] is equal to numbers[1]
        if numbers[0] == numbers[1]:
            closest1, closest2 = numbers[1], numbers[0]
        else:
            closest1, closest2 = numbers[0], numbers[1]
    # Return the two closest numbers
    return closest1, closest2

``` 
This function takes in a list of numbers and selects the two closest elements in the list. It then returns the numbers in order, with the smaller number being first.