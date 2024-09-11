```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list excluding the last element
    for i in range(len(sorted_numbers) - 1):
        # Check if the current number and the next one are closer than the threshold
        if sorted_numbers[i + 1] - sorted_numbers[i] < threshold:
            # If they are, return True immediately
            return True
    
    # If no such pair is found after checking all numbers, return False
    return False


# Example usage:
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It sorts the list in ascending order and then checks each pair of adjacent numbers to see if they are closer than the threshold. If such a pair is found, the function returns `True`. If no such pair is found after checking all numbers, the function returns `False`. The script includes example usage at the end to demonstrate the function's behavior.