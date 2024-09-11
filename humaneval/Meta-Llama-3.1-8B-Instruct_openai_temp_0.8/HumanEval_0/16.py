```markdown
### has_close_elements Function
#### Checks if any two numbers in a list are closer than a given threshold

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    numbers (List[float]): The list of numbers to check.
    threshold (float): The minimum distance between two numbers.

    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # Check if the distance between the two numbers is less than the threshold
            if abs(numbers[i] - numbers[j]) < threshold:
                return True  # If a pair is found, immediately return True
    return False  # If no pair is found after checking all numbers, return False
```

### Example Use Cases

```python
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

This function works by iterating over the list of numbers and checking each pair of numbers to see if they are closer than the given threshold. If it finds a pair of numbers that are closer than the threshold, it immediately returns `True`. If it checks all pairs of numbers and doesn't find any that are closer than the threshold, it returns `False`.