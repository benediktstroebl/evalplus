### Self-Contained Python Script

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers for them to be considered close.

    Returns:
    bool: True if two numbers are closer than the threshold, False otherwise.
    """
    if len(numbers) <= 1:
        # If there is one or zero numbers in the list, no two numbers can be close.
        return False

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Calculate the absolute difference between two numbers.
            if abs(numbers[i] - numbers[j]) < threshold:
                # If the difference is less than the threshold, return True.
                return True

    # If no two numbers were found to be close, return False.
    return False

# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a given list are closer than a specified threshold. It then tests this function with the provided test cases.