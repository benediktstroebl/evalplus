### Find Closest Elements in a List of Numbers
#### Python Script
```python
from typing import List, Tuple
import math

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Find two numbers in a list that are the closest to each other and return them in order.

    Args:
        numbers (List[float]): A list of numbers of length at least two.

    Returns:
        Tuple[float, float]: A tuple containing two numbers that are the closest to each other.
    """

    # Check if the list has less than two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Sort the list
    numbers.sort()

    # Initialize variables to store the closest pair and the minimum difference
    closest_pair = (numbers[0], numbers[0])
    min_diff = float('inf')  # Initialize with positive infinity

    # Iterate over the sorted list to find the closest pair
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current element and the next one
        diff = numbers[i + 1] - numbers[i]

        # If the difference is less than the current minimum difference, update the closest pair and the minimum difference
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])

    return closest_pair

# Test cases
if __name__ == "__main__":
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # (2.0, 2.2)
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # (2.0, 2.0)
```
This script defines a function `find_closest_elements` that takes a list of numbers as input, sorts it, and then iterates over the sorted list to find the closest pair of numbers. The closest pair is returned as a tuple. The script also includes test cases to demonstrate its usage.