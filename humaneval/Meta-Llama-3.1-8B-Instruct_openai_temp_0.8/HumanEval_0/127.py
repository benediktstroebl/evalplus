### Python Script to Check for Close Elements in a List

```python
from typing import List
import itertools


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): The list of numbers to check.
    threshold (float): The minimum distance required between numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Generate pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check each pair to see if their difference is less than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) < threshold:
            return True
    
    # If no pairs were found with a difference less than the threshold, return False
    return False


# Example use cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script defines the `has_close_elements` function, which takes a list of numbers and a threshold distance as input. It uses the `itertools.combinations` function to generate all pairs of numbers in the list, then checks each pair to see if their difference is less than the threshold. If it finds any pair that meets this condition, it immediately returns `True`. If it checks all pairs without finding any that meet the condition, it returns `False`.

The example use cases at the end of the script demonstrate how to use this function.