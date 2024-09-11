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
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, we sort the list of numbers in ascending order
    numbers.sort()
    
    # Then, we initialize a variable to store the previous number in the list
    previous_number = numbers[0]
    
    # We iterate over the sorted list of numbers starting from the second number
    for current_number in numbers[1:]:
        # For each number, we calculate the difference between the current number and the previous number
        difference = abs(current_number - previous_number)
        
        # If the difference is less than or equal to the threshold, we return True
        if difference <= threshold:
            return True
        
        # Otherwise, we update the previous number and continue with the next number in the list
        previous_number = current_number
    
    # If we have iterated over the entire list and haven't found any two numbers that are closer than the threshold,
    # we return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```