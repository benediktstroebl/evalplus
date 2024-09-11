```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The maximum allowed difference between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # First, sort the list of numbers in ascending order
    numbers.sort()

    # Iterate through the sorted list of numbers
    for i in range(len(numbers) - 1):
        # Calculate the absolute difference between the current number and the next one
        difference = abs(numbers[i] - numbers[i + 1])
        
        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True

    # If no pairs of numbers with a difference less than or equal to the threshold are found, return False
    return False


# Test the function with some examples
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print: True
```