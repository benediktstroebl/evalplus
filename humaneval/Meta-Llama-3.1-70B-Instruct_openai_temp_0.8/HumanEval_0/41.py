```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if there are two numbers closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers. This is because we can then compare adjacent
    # numbers to find the closest pairs.
    numbers.sort()
    
    # Initialize a variable to store the result. We assume that there are no close
    # elements at the start.
    has_close = False
    
    # Iterate over the sorted list of numbers.
    for i in range(len(numbers) - 1):
        # For each number, calculate the difference with the next number.
        difference = numbers[i + 1] - numbers[i]
        
        # If the difference is less than or equal to the threshold, we have found two
        # numbers that are closer than the threshold.
        if difference <= threshold:
            has_close = True
            # We can stop iterating as soon as we find a pair of close numbers.
            break
    
    # Return the result.
    return has_close


# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    print(False)
else:
    print(True)

if has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    print(True)
else:
    print(False)
```