```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
    numbers (List[float]): A list of float numbers

    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in order

    Raises:
    ValueError: If the list contains less than two elements
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])

    # Iterate over the list to find the pair of closest numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of float numbers and returns a tuple containing the two closest numbers in order. It first checks if the list contains at least two elements, then sorts the list in ascending order. It initializes the minimum difference and the pair of closest numbers, and then iterates over the list to find the pair of closest numbers. If the difference between two adjacent numbers is less than the current minimum difference, it updates the minimum difference and the pair of closest numbers. Finally, it returns the pair of closest numbers. The test cases are included at the end of the script to demonstrate the function's usage.