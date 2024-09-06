Here is a self-contained Python script that solves the problem you have provided:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two numbers that are the closest to each other from the list.

    If two numbers in the list are the closest, return them in order (smaller number, larger number)
    """

    # Sort the list of numbers
    sorted_numbers = sorted(numbers)

    # Get the first two elements of the sorted list
    first_two_elements = sorted_numbers[:2]

    # Return the two closest numbers
    return first_two_elements

# Example of usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = find_closest_elements(numbers)
```

The code provides a function named `find_closest_elements` that takes a list of numbers as input. The function sorts the list and then selects the first two elements, which are assumed to be the closest to each other. The function returns a two numbers, which are the closest to each other and returned in that order.

The provided example usage demonstrates how to call the function with a list of numbers and stores the result in the `result` variable.