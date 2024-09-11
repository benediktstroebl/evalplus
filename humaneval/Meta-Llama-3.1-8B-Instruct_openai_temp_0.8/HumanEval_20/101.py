```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of numbers of length at least two.

    Returns:
        Tuple[float, float]: A tuple of two numbers that are the closest to each other.
    """
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the sorted list to find the pair of numbers with the minimum difference
    for i in range(1, len(numbers)):
        # Calculate the difference between the current number and the previous number
        diff = numbers[i] - numbers[i - 1]
        
        # If the current difference is less than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i - 1], numbers[i])
    
    return closest_pair

# Test the function
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other. The function sorts the list of numbers in ascending order and then iterates over the sorted list to find the pair of numbers with the minimum difference. The function returns this pair of numbers. The script also includes two test cases to verify the correctness of the function.