Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the input list of numbers
    numbers.sort()
    values in descending order
    # Find the two closest elements
    left, right = min(numbers), max(numbers))
    closest = (left, right)
    # Return the closest elements in descending order
    return (right, closest[0])

```

This function takes a list of numbers as input and returns a tuple containing the two closest elements in descending order. It uses the Python's `min()` and `max()` functions to find the two closest elements in the list. 

Note that the `find_closest_elements` function returns the result directly, which can be used as an example to solve the problem.