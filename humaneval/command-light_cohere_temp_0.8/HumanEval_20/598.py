```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    return (closest_val1, closest_val2)
    """
    if len(numbers) < 2:
        raise ValueError("Need at least two elements to find the closest pair")
    # Sort the numbers in descending order
    numbers.sort(reverse=True)

    # Initialize the closest values
    closest_val1 = float('inf')
    closest_val2 = float('-inf')

    # Initialize the index
    i = 0
    j = 1

    # Loop until there are at least two elements in the list
    while i < len(numbers) - 1 and j < len(numbers) - 1:
        # Calculate the distance between the two elements
        dist = numbers[i] - numbers[j]
        # Check if the distance is smaller than the current closest values
        if dist < closest_val1:
            closest_val1 = dist
            closest_val2 = numbers[j]
        else:
            closest_val2 = dist
            closest_val1 = numbers[i]
        i += 1
        j += 1
    return closest_val1, closest_val2

```

This function, `find_closest_elements`, accepts a list of numbers as an argument and returns a tuple of two closest numbers. The function first checks if the is only one element in the list. If so, it raises a `ValueError`.

The function then sorts the list of numbers in descending order. It initializes two closest values to `float('inf')` and `float('-inf')`, respectively, and initializes the index to `0` and `1`. The function then loops until there are at least two elements in the list. In each iteration, it calculates the distance between the current elements and checks if the distance is smaller than the current closest values. If so, it updates the closest values accordingly.

Finally, the function returns the two closest numbers.

This function can be a good starting point for solving the problem and passing the tests. It provides a structure and logic that can be further improved and optimized.