```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    
    # First, sort the list of numbers in ascending order
    numbers.sort()
    
    # Iterate over the sorted list, checking the difference between adjacent numbers
    for i in range(1, len(numbers)):
        # If the difference is less than or equal to the threshold, return True
        if numbers[i] - numbers[i - 1] <= threshold:
            return True
    
    # If the loop completes without finding any close elements, return False
    return False


# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print: True
```