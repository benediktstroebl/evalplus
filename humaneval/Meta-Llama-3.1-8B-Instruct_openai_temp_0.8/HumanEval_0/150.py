### has_close_elements.py
```markdown
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of floating point numbers.
        threshold (float): The minimum distance two numbers should have.

    Returns:
        bool: True if any two numbers are closer than threshold, False otherwise.
    """
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines a function `has_close_elements` that iterates over all pairs of numbers in the input list. If it finds a pair where the difference is less than the given threshold, it immediately returns `True`. If it has checked all pairs without finding any close elements, it returns `False`. The example usage at the end demonstrates how to use the function in a script.