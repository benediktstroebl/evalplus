```markdown
### Close Elements Check Script

#### Description
This script checks if there are any two numbers in a list that are closer to each other
than a given threshold.

#### Code
```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The maximum allowed difference between two numbers.

    Returns:
    bool: True if there are two numbers in the list closer than the threshold, False otherwise.
    """
    # Generate combinations of two numbers from the list
    pairs = itertools.combinations(numbers, 2)
    
    # Check each pair to see if their difference is less than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) < threshold:
            return True
    
    # If no pairs are found with a difference less than the threshold, return False
    return False

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

#### Explanation
This script defines a function `has_close_elements` that takes a list of numbers and a threshold.
It generates all possible pairs of numbers from the list using `itertools.combinations`.
For each pair, it checks if their absolute difference is less than the threshold.
If it finds any pair with a difference less than the threshold, it returns True.
If it checks all pairs without finding any with a difference less than the threshold, it returns False.

Note: The script uses the `itertools.combinations` function to generate pairs, which is more memory-efficient than generating pairs in a loop, especially for large lists of numbers.