```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance required between any two numbers.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers to make it easier to compare adjacent elements
    numbers.sort()
    
    # Iterate over the list of numbers, comparing each element with its adjacent elements
    for i in range(1, len(numbers)):
        # If the difference between the current element and its previous element is less than the threshold
        if numbers[i] - numbers[i - 1] < threshold:
            # Return True, indicating that two numbers are closer than the threshold
            return True
    
    # If the loop completes without finding any two numbers closer than the threshold, return False
    return False

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input, and returns a boolean indicating whether any two numbers in the list are closer than the threshold. It sorts the list of numbers, then iterates over the list, comparing each element with its adjacent elements. If it finds any two numbers that are closer than the threshold, it immediately returns True. If it doesn't find any such numbers after iterating over the entire list, it returns False.