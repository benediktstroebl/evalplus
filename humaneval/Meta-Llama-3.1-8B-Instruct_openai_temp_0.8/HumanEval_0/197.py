```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered 'close'.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Use itertools.combinations to generate all possible pairs of numbers
    for num1, num2 in itertools.combinations(numbers, 2):
        # Check if the difference between the two numbers is less than the threshold
        if abs(num1 - num2) < threshold:
            return True
    # If no pairs are found to be within the threshold, return False
    return False

# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
    print(has_close_elements([1.0, 2.0, 3.0], 0.8))  # False
    print(has_close_elements([0.0, 0.8, 1.0, 1.2], 0.2))  # True
```

This script defines a function `has_close_elements` that checks if any two numbers in a list are closer than a given threshold. It uses the `itertools.combinations` function to generate all possible pairs of numbers, and returns True as soon as it finds a pair that is closer than the threshold. If it checks all pairs and finds none that are closer than the threshold, it returns False. The script includes test cases to demonstrate its correctness.