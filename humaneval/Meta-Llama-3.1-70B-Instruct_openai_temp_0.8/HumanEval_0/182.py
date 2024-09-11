```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()

    # Then, we iterate over the sorted list with a for loop and an index
    for i in range(len(numbers) - 1):
        # For each number, we check if the difference between it and the next number is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            # If we find a pair of numbers that are closer than the threshold, we immediately return True
            return True

    # If we finish iterating over the list without finding any pairs of numbers that are closer than the threshold, we return False
    return False


# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```
Note that the time complexity of this script is O(n log n) due to the sorting operation, where n is the number of elements in the input list. If you want a solution with a time complexity of O(n), you would need to use a different approach, such as using a hash table to keep track of the numbers you've seen so far and their closest neighbors.