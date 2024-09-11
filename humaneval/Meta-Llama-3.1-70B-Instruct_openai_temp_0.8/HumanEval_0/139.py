```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): The list of numbers to check.
        threshold (float): The minimum distance required between numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Initialize a variable to store the result
    has_close_elements = False

    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current number and the next number
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, update the result
        if difference <= threshold:
            has_close_elements = True
            # Break out of the loop as soon as we find a pair of close elements
            break

    return has_close_elements


# Test the function
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```