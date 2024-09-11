```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if two numbers are closer than the threshold, False otherwise.
    """
    # Generate all possible pairs of numbers
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check each pair to see if it's closer than the threshold
    for num1, num2 in pairs:
        if abs(num1 - num2) < threshold:
            return True  # If we find a pair that's closer than the threshold, return True immediately
    
    # If we've checked all pairs and haven't returned True, then no pair is closer than the threshold
    return False

# Test cases
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

In this script, I've used the `itertools.combinations` function to generate all possible pairs of numbers. I then iterate over these pairs, checking each one to see if it's closer than the given threshold. If I find a pair that is, I immediately return `True`. If I've checked all pairs and haven't returned `True`, then no pair is closer than the threshold, and I return `False`.