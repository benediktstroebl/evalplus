```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The threshold value.

    Returns:
        bool: True if there are two numbers closer than the threshold, False otherwise.

    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    # Generate all pairs of numbers
    pairs = itertools.combinations(numbers, 2)
    
    # Check each pair to see if the difference is less than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) < threshold:
            # If we find a pair closer than the threshold, return True
            return True
    
    # If we check all pairs and don't find any closer than the threshold, return False
    return False


# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print: True
```