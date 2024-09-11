```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than 
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance two numbers must be apart.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize a variable to store the previous number in the list
    previous_number = None
    
    # Iterate over the sorted list of numbers
    for current_number in numbers:
        # If this is not the first number in the list
        if previous_number is not None:
            # Check if the difference between the current number and the previous number is less than the threshold
            if current_number - previous_number < threshold:
                # If it is, return True immediately
                return True
        # Update the previous number for the next iteration
        previous_number = current_number
    
    # If we've iterated over the entire list and haven't found any numbers closer than the threshold, return False
    return False

# Test cases
if has_close_elements([1.0, 2.0, 3.0], 0.5):
    assert False, "Test case failed"
else:
    assert True

if not has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3):
    assert False, "Test case failed"
else:
    assert True
```