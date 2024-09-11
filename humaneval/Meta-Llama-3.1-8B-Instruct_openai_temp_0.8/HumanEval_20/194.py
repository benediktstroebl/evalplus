### Find Closest Elements in a List of Numbers
#### Problem Description
From a supplied list of numbers (of length at least two), select and return two that are the closest to each other and return them in order (smaller number, larger number).

#### Solution
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two numbers in the list that are the closest to each other.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    Tuple[float, float]: A tuple of two numbers that are the closest to each other.
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize the minimum difference and the closest pair
    min_diff = float('inf')
    closest_pair = (numbers[0], numbers[0])
    
    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next one
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script sorts the list of numbers and then iterates over the sorted list to find the closest pair of numbers. It keeps track of the minimum difference and the closest pair found so far. The time complexity of this solution is O(n log n) due to the sorting step, where n is the number of elements in the list. The space complexity is O(n) for the sorted list.