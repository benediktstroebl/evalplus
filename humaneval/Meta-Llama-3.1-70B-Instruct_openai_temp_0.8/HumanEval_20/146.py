```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in ascending order.
    """
    
    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()

    # Iterate through the sorted list to find the pair of numbers with the minimum difference
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

This script defines a function `find_closest_elements` that takes a list of floating point numbers as input and returns a tuple containing the two closest numbers in ascending order. The function first checks if the list contains at least two elements, then sorts the list in ascending order. It then iterates through the sorted list to find the pair of numbers with the minimum difference. The pair with the minimum difference is returned as a tuple. The script also includes test cases to demonstrate the function's behavior.