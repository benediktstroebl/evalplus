```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    Args:
        numbers (List[float]): A list of at least two floating-point numbers.

    Returns:
        Tuple[float, float]: A tuple containing two numbers from the input list that are closest to each other.
    """
    
    # Sort the list of numbers
    numbers.sort()
    
    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the smallest number
    
    # Iterate over the sorted list to find the pair with the minimum difference
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        
        # If the current difference is smaller than the minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    
    return closest_pair

# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script works by sorting the list of numbers first. Then, it iterates over the sorted list to find the pair of numbers with the minimum difference. The pair with the minimum difference is returned as a tuple. If the list contains duplicate numbers, the script will return the first occurrence of such numbers. If you want to return all occurrences of the closest pair, you would need to modify the script accordingly.