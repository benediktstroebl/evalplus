```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of float numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list
    for i in range(1, len(numbers)):
        # Calculate the distance between the current number and the previous one
        distance = numbers[i] - numbers[i-1]
        
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True
    
    # If no two numbers are closer than the threshold, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script first sorts the list of numbers in ascending order. Then, it iterates over the sorted list, calculating the distance between each pair of consecutive numbers. If it finds a pair of numbers with a distance less than the threshold, it immediately returns `True`. If it doesn't find any such pair after checking all numbers, it returns `False`.