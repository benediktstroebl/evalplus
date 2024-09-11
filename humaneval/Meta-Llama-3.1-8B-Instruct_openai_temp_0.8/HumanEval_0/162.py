```markdown
### Close Elements Checker
#### Problem Description
Checks if in a given list of numbers, any two numbers are closer to each other than a given threshold.

#### Solution

```python
from typing import List
import itertools

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): A list of floating point numbers.
    threshold (float): The minimum distance between two numbers to be considered close.

    Returns:
    bool: True if any two numbers in the list are closer than the given threshold, False otherwise.
    """
    # Generate all pairs of numbers in the list
    pairs = list(itertools.combinations(numbers, 2))
    
    # Check each pair to see if any are closer than the threshold
    for pair in pairs:
        if abs(pair[0] - pair[1]) <= threshold:
            return True
    
    # If no pairs are closer than the threshold, return False
    return False

### Example Usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This script uses the `itertools.combinations` function to generate all pairs of numbers in the list, then checks each pair to see if any are closer than the given threshold. If it finds a pair that is closer, it immediately returns `True`. If it checks all pairs and finds none that are closer, it returns `False`.