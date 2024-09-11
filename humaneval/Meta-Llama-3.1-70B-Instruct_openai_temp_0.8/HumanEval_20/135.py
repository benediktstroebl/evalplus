```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    :param numbers: A list of numbers
    :return: A tuple containing the closest two numbers in order
    """
    numbers.sort()  # First, sort the list of numbers
    
    # Initialize the minimum difference and the corresponding pair of numbers
    min_diff = float('inf')  # Initialize with positive infinity
    closest_pair = ()  # Initialize with an empty tuple
    
    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]  # Calculate the difference between adjacent numbers
        if diff < min_diff:  # If a smaller difference is found
            min_diff = diff  # Update the minimum difference
            closest_pair = (numbers[i], numbers[i + 1])  # Update the closest pair
    
    return closest_pair


# Test cases
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Expected output: (2.0, 2.2)
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Expected output: (2.0, 2.0)
```

This script defines a function `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the closest two numbers in order. It first sorts the list of numbers, then iterates over the sorted list to find the closest pair. The minimum difference and the corresponding pair of numbers are updated whenever a smaller difference is found. The function finally returns the closest pair. The script also includes two test cases to verify the correctness of the function.