```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of floating point numbers of length at least two.

    Returns:
        Tuple[float, float]: A tuple containing the two numbers that are the closest to each other.
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with infinity
    closest_pair = ()
    
    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that takes a list of numbers, sorts it, and then iterates over the sorted list to find the pair of numbers with the minimum difference. The function returns this pair of numbers in order (smaller number, larger number). The script also includes two test cases to demonstrate the function's behavior.