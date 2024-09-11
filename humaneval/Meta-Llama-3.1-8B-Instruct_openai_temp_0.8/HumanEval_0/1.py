### Close Elements Checker

Below is a Python script that uses the provided function signature and implements the `has_close_elements` function.

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers
    threshold (float): The minimum distance between two numbers to be considered 'close'

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list
    for i in range(1, len(sorted_numbers)):
        # Check if the difference between current and previous number is less than the threshold
        if sorted_numbers[i] - sorted_numbers[i - 1] < threshold:
            # If 'close' numbers are found, return True
            return True
    
    # If no 'close' numbers are found, return False
    return False

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
```

This script first sorts the list of numbers and then iterates through the sorted list to check the difference between each pair of adjacent numbers. If a difference less than the threshold is found, the function immediately returns `True`. If no such pairs are found after checking all numbers, the function returns `False`.