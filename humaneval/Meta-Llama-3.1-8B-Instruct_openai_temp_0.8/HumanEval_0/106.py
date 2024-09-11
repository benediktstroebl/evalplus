### Close Elements Checker
```markdown
# Close Elements Checker

This script checks if in a given list of numbers, are any two numbers closer to each other than a given threshold.

### Code

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance required between two numbers to consider them "close".

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Iterate over the sorted list
    for i in range(1, len(sorted_numbers)):
        # Calculate the distance between the current number and the previous number
        distance = sorted_numbers[i] - sorted_numbers[i - 1]
        # Check if the distance is less than the threshold
        if distance < threshold:
            # If it is, return True
            return True
    
    # If we've checked all numbers and haven't found any close pairs, return False
    return False

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

### Explanation

This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input. It sorts the list of numbers, then iterates over the sorted list. For each pair of adjacent numbers, it calculates the distance between them. If the distance is less than the threshold, it immediately returns `True`. If it checks all pairs of numbers and doesn't find any close pairs, it returns `False`.

The example usage at the end demonstrates how to use the function.