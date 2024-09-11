```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Create a copy of the list and sort it in ascending order
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list of numbers
    for i in range(1, len(sorted_numbers)):
        # Calculate the difference between the current number and the previous one
        difference = sorted_numbers[i] - sorted_numbers[i-1]
        
        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True
    
    # If no close elements are found, return False
    return False

# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```