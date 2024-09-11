```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of numbers to check.
        threshold (float): Minimum distance between two numbers to be considered "close".

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """

    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))

    # Check each pair to see if the distance is less than the threshold
    for pair in pairs:
        # Calculate the absolute difference between the two numbers
        distance = abs(pair[0] - pair[1])
        
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True

    # If no pairs with distance less than threshold were found, return False
    return False

# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the `itertools.combinations` function to generate all possible pairs of numbers in the list. It then checks each pair to see if the distance between the two numbers is less than the given threshold. If it finds a pair with distance less than the threshold, it immediately returns `True`. If it checks all pairs and finds none with distance less than the threshold, it returns `False`.