```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    This function finds the two closest numbers in a list and returns them in order.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        Tuple[float, float]: A tuple of two closest numbers in the list, in ascending order.
    """
    
    # First, we sort the list in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()
    
    # Iterate over the sorted list to find the pair with the minimum difference
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

This script defines a function `find_closest_elements` that takes a list of numbers as input, sorts the list, and then iterates over the sorted list to find the pair of numbers with the minimum difference. The function returns this pair of numbers in ascending order. The script also includes test cases to demonstrate the function's correctness.