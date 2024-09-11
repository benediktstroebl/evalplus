### Closest Pair Finder

Below is a Python script that implements a function `find_closest_elements` to find the closest pair of numbers in a list.

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    Args:
    numbers (List[float]): A list of float numbers.
    
    Returns:
    Tuple[float, float]: A tuple containing the two closest numbers in the list.
    """
    
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of numbers with the minimum difference
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = (numbers[0], numbers[0])  # Initialize with the first two numbers
    
    # Iterate over the list of numbers to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the current difference is less than the minimum difference found so far, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    return closest_pair

# Test cases
if __name__ == "__main__":
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))
```

This script first sorts the list of numbers in ascending order. It then iterates over the sorted list to find the pair of numbers with the minimum difference. The minimum difference and the closest pair are updated whenever a smaller difference is found. The function returns the closest pair of numbers.