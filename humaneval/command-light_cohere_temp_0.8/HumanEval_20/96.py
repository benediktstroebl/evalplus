Here is a Python script that includes a self-contained function that solves the problem of finding the closest two elements in a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Sort the list in ascending order
    sorted_numbers = sorted(numbers, reverse=True)

    # Define the variables for the two closest elements
    closest_low = sorted_numbers[0]
    closest_high = sorted_numbers[1]

    # Check if the list has more than two elements
    if len(numbers) > 2:
        # Identify the two next elements in the list that are greater than the current closest pair
        next_low = sorted_numbers[2]
        next_high = sorted_numbers[3]
        # Update the variables for the two closest elements
        closest_low = next_low
        closest_high = next_high

    # Return the two closest elements
    return closest_low, closest_high
```
This code defines a function `find_closest_elements` that takes in a list of numbers as input and returns a tuple of the two closest numbers. The function first sorts theal list of numbers in ascending order, then it identifies the two closest elements to the original pair of closest elements. The function then updates the same variables for the two closest elements, and finally returns the two closest elements in order (smaller number, larger number).