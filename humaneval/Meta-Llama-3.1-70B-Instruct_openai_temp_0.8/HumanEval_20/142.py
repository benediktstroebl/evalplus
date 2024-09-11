```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple of two numbers that are closest to each other in the list.

    Raises:
        ValueError: If the input list has less than two elements.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    # Sort the list of numbers
    numbers.sort()

    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = ()

    # Iterate through the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```

In this script, we define the function `find_closest_elements` that takes a list of floating point numbers as input and returns a tuple of two numbers that are closest to each other in the list. The function first checks if the input list has at least two elements, and raises a `ValueError` if it does not. Then, it sorts the list of numbers and iterates through the sorted list to find the closest pair. Finally, it returns the closest pair as a tuple.

We also provide two test cases to demonstrate the usage of the function.