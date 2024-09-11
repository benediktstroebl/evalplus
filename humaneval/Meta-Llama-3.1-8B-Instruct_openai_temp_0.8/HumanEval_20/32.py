```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers: A list of at least two floating point numbers.

    Returns:
        A tuple of two numbers that are the closest to each other.
    """
    numbers.sort()  # sort the list to simplify finding closest elements
    min_diff = float('inf')  # initialize minimum difference as infinity
    closest_pair = ()  # initialize closest pair as an empty tuple

    # iterate over the list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # calculate the difference between current and next number
        if diff < min_diff:  # if the difference is less than the current minimum difference
            min_diff = diff  # update the minimum difference
            closest_pair = (numbers[i], numbers[i + 1])  # update the closest pair

    return closest_pair  # return the closest pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other. The function sorts the list and then iterates over it to find the closest pair. It keeps track of the minimum difference and the closest pair as it iterates over the list. The script includes two test cases to demonstrate the function's behavior.