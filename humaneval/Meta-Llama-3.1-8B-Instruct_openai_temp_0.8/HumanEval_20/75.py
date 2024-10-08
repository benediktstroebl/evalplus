```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of at least two numbers.

    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers to each other.
    """
    
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of numbers with that difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the sorted list of numbers to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script defines a function `find_closest_elements` that finds the two closest numbers in a given list of numbers. The function sorts the list in ascending order, then iterates over the sorted list to find the pair of numbers with the minimum difference. The script includes two test cases to verify the correctness of the function.