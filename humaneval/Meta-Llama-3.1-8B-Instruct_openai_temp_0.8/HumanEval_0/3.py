### Close Elements Checker

The following Python script defines a function `has_close_elements` to check if any two numbers in a given list are closer to each other than a specified threshold.

```markdown
### Code
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
    - numbers (List[float]): A list of floating-point numbers.
    - threshold (float): The minimum distance between two numbers to be considered distinct.

    Returns:
    - bool: True if any two numbers in the list are closer to each other than the threshold, False otherwise.
    """
    
    # Sort the list of numbers
    numbers.sort()

    # Iterate over the list of numbers
    for i in range(len(numbers) - 1):
        # Check if the difference between the current number and the next one is less than the threshold
        if numbers[i + 1] - numbers[i] < threshold:
            return True  # If yes, return True immediately

    return False  # If no such pair is found, return False


### Example Usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True
```

### Explanation

This script defines a function `has_close_elements` that takes two inputs:

*   `numbers`: A list of floating-point numbers.
*   `threshold`: The minimum distance between two numbers to be considered distinct.

The function sorts the list of numbers in ascending order. Then, it iterates over the sorted list, checking if the difference between each pair of adjacent numbers is less than the given threshold. If such a pair is found, the function returns `True` immediately. If no such pair is found after iterating over the entire list, the function returns `False`.

The script also includes example usage to demonstrate the function's behavior.