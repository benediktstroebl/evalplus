```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers
    threshold (float): The minimum distance between two numbers to be considered as close

    Returns:
    bool: True if any two numbers in the list are closer to each other than the given threshold, False otherwise
    """
    # Sort the list of numbers to make it easier to find close elements
    numbers.sort()
    
    # Iterate over the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the distance between the current number and the next number
        distance = numbers[i + 1] - numbers[i]
        
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True
    
    # If no close elements were found, return False
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It sorts the list of numbers and then iterates over the sorted list to check if any two numbers are closer to each other than the given threshold. If such a pair is found, the function returns True; otherwise, it returns False. The script also includes example usage of the function.