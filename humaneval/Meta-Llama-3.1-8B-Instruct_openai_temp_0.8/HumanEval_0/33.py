```markdown
### Close Elements Checker

This script checks if any two numbers in a given list are closer to each other than a specified threshold.

#### Code

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): List of floating point numbers.
        threshold (float): Minimum distance between two numbers to be considered close.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list to compare each pair of adjacent numbers
    for i in range(len(sorted_numbers) - 1):
        # Calculate the distance between the current and next number
        distance = sorted_numbers[i + 1] - sorted_numbers[i]
        
        # If the distance is less than the threshold, return True
        if distance < threshold:
            return True
    
    # If no close elements are found, return False
    return False

### Example Usage

if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

#### Explanation

This script defines a function `has_close_elements` that takes a list of floating point numbers and a threshold as input. It sorts the list in ascending order and then iterates over the sorted list to compare each pair of adjacent numbers. If the distance between any two adjacent numbers is less than the threshold, it returns `True`. If no close elements are found after checking all pairs, it returns `False`. The example usage demonstrates how to use the function with different input lists and thresholds.