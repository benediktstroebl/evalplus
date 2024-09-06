Here's the Python script:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).
    returns a tuple of the two closest numbers
    """
    # Sort the list of numbers
    numbers.sort(key=lambda x: x, -x)
    # Initialize the closest pair variables
    closest_pair = None
    closest_num = None
    # Loop over the list of numbers and find the two closest numbers
    for x, y in zip(numbers, numbers[1:]):
        if closest_pair is None or (x > closest_num and y < closest_pair):
            closest_pair = (x, y)
            closest_num = x
    return closest_pair
```

This code uses the **zip** function to iterate over the list of numbers and find the two closest numbers. It then initializes variables for the closest pair and closest number, then iterates over the list, comparing each pair of numbers to see if they are the closest pair or not, and updates the variables accordingly.