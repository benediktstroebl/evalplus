```markdown
### Close Elements Checker
#### Function to Check if Two Numbers in a List are Closer than a Given Threshold

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.

    Args:
        numbers (List[float]): The list of numbers to check.
        threshold (float): The minimum distance between two numbers to be considered "far enough".

    Returns:
        bool: True if any two numbers in the list are closer than the threshold, False otherwise.

    Example:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False

# Test the function
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Should print: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Should print: True
```

### Explanation:
This script defines a function `has_close_elements` that takes a list of numbers and a threshold as input and returns True if any two numbers in the list are closer than the threshold, and False otherwise.

### How it works:
1. The function iterates over each pair of numbers in the list, starting from the first number and comparing it with all the numbers that come after it.
2. For each pair of numbers, it checks if the absolute difference between them is less than the threshold.
3. If it finds a pair of numbers that are closer than the threshold, it immediately returns True.
4. If it has checked all pairs of numbers without finding any that are closer than the threshold, it returns False.

### Testing:
The script includes two example tests to demonstrate the function's behavior. The first test checks a list of numbers where all numbers are far enough from each other, and the second test checks a list of numbers where two numbers are close to each other.