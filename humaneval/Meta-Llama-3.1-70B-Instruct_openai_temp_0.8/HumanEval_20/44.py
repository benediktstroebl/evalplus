```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers: A list of floats with a length of at least two.

    Returns:
    A tuple containing the two closest numbers in order.
    """
    # First, we sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the corresponding pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()

    # Iterate over the sorted list to find the closest pair of numbers
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

This Python script defines a function `find_closest_elements` that takes a list of floats as input and returns a tuple containing the two closest numbers in order. The function first sorts the input list in ascending order. Then, it iterates over the sorted list to find the closest pair of numbers by keeping track of the minimum difference and the corresponding pair of numbers. The function returns the closest pair of numbers.

The script includes two test cases to demonstrate the function's correctness. The expected output of each test case is provided as a comment.