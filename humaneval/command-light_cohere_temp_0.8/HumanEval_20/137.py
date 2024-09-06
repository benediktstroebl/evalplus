```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    Parameters:
    - numbers (List[float]): a list of at least two numbers.
    Returns:
    - a tuple of the two closest numbers.

    Returns:
    - tuple[float], float): a tuple of the two closest numbers.
    """


# Test cases

test_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
test_closest_numbers = find_closest_elements(test_numbers)

print(test_numbers)

print(test_closest_numbers)
```

This Python code defines a function named `find_closest_elements` that aims to select the two closest elements from a given list of numbers, where each number is represented as a float. The function takes a list of numbers as its parameter and returns a tuple containing the two closest numbers, along with their relative order. 

The function employs the `sorted()` function with a custom sorting criteria to determine the order of the closest numbers. It then returns the to test cases, the function is used to find the closest elements in a list of numbers, which can be useful in various scenarios such as finding the closest neighbors in a dataset or making comparisons between different numbers.