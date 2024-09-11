```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if two numbers in the list are closer than the threshold, False otherwise.
    """
    # If the list has less than two elements, no two numbers can be close
    if len(numbers) < 2:
        return False
    
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list and check for pairs of numbers with a distance less than the threshold
    for i in range(1, len(sorted_numbers)):
        distance = sorted_numbers[i] - sorted_numbers[i - 1]
        if distance < threshold:
            return True
    
    # If no close numbers were found, return False
    return False

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function as specified and includes example usage at the end. It sorts the list of numbers and then iterates over the sorted list to check for pairs of numbers with a distance less than the threshold. If it finds any such pair, it immediately returns `True`. If it finishes iterating over the list without finding any close numbers, it returns `False`.