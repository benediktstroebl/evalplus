### has_close_elements Function
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): The list of numbers to check.
        threshold (float): The minimum distance between two numbers to be considered as close.

    Returns:
        bool: True if two numbers are closer to each other than the threshold, False otherwise.
    """
    # Sort the list of numbers
    numbers.sort()
    
    # Iterate over the sorted list to check for close elements
    for i in range(len(numbers) - 1):
        # If the difference between two consecutive numbers is less than the threshold, return True
        if numbers[i+1] - numbers[i] < threshold:
            return True
    
    # If no close elements are found, return False
    return False

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```
This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer to each other than a specified threshold. The function first sorts the list of numbers and then iterates over the sorted list to check for close elements. If it finds any two consecutive numbers with a difference less than the threshold, it immediately returns `True`. If it finishes checking all pairs of numbers without finding any close elements, it returns `False`. The script also includes example usage at the end to demonstrate the function's behavior.