```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    Args:
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    Tuple[float, float]: A tuple of the two closest numbers in ascending order.
    """
    
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize the minimum difference and the pair of closest numbers with the first two elements in the sorted list
    min_diff = numbers[1] - numbers[0]
    closest_pair = (numbers[0], numbers[1])
    
    # Iterate over the sorted list to find the pair of closest numbers
    for i in range(1, len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = numbers[i + 1] - numbers[i]
        
        # If the difference is smaller than the current minimum difference, update the minimum difference and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    
    # Return the pair of closest numbers
    return closest_pair


# Test the function
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```

In this script, the `find_closest_elements` function takes a list of floating point numbers as input, sorts the list in ascending order, and then iterates over the sorted list to find the pair of closest numbers. The function returns the pair of closest numbers in ascending order. The script also includes test cases to verify the correctness of the function.