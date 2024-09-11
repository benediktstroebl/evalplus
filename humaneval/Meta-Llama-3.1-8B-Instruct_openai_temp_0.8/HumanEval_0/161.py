```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of float numbers.
    threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
    bool: True if any two numbers are closer than the given threshold, False otherwise.
    """
    numbers.sort()  # Sort the list in ascending order
    
    for i in range(1, len(numbers)):  # Iterate over the list starting from the second element
        if numbers[i] - numbers[i-1] < threshold:  # Check the distance between current and previous element
            return True  # If the distance is less than the threshold, return True
    
    return False  # If no pair of elements is closer than the threshold, return False

# Test cases
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, sorts the list, and then checks each pair of adjacent elements to see if they are closer than the threshold. If any pair is closer, the function immediately returns `True`. If no pair is closer, the function returns `False`. The script then includes test cases to verify that the function works correctly.