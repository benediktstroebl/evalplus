### Closest Pair Finder

The following Python script defines a function `find_closest_elements` that takes a list of numbers and returns the two closest numbers to each other.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Select and return two numbers from the supplied list that are the closest to each other.
    
    Args:
        numbers (List[float]): A list of numbers of length at least two.
    
    Returns:
        Tuple[float, float]: A tuple containing the two closest numbers in order (smaller number, larger number).
    """
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()
    
    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is less than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the pair of closest numbers
    return closest_pair

# Example usage:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```

This script uses a simple and efficient approach to find the pair of closest numbers in the list. It first sorts the list in ascending order, then iterates over the sorted list to find the pair with the minimum difference. The time complexity of this approach is O(n log n) due to the sorting step, where n is the length of the input list. However, the subsequent iteration has a time complexity of O(n), making the overall time complexity O(n log n).