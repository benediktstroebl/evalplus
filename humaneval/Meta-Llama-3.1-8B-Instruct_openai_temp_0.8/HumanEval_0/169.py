```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers to be considered distinct.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the numbers to bring close elements together
    numbers.sort()
    
    # Iterate over the sorted list
    for i in range(1, len(numbers)):
        # Calculate the distance between the current and previous number
        distance = numbers[i] - numbers[i-1]
        
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True
    
    # If no pairs of elements with distance less than threshold are found, return False
    return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
print(has_close_elements([10.0, 20.0, 30.0, 40.0, 50.0], 5.0))  # False
```
This script uses the `sort` method to sort the list of numbers, and then iterates over the sorted list to check the distance between consecutive elements. If it finds any pair of elements with a distance less than the threshold, it returns `True`. If it doesn't find any such pair after checking all elements, it returns `False`.