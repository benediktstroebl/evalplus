Here's a self-contained Python script that implements the function has_close_elements from your prompt:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks if all pairs of numbers in the given list are closer than the given threshold.
    Returns True if there are any two elements in the list that are closer than the threshold, False otherwise.
    """
    return any_two_are_close(numbers, threshold)

def any_two_are_close(numbers: List[float], threshold: float) -> bool:
    """
    Check if all pairs of elements in the list are closer than the given threshold.
    Args:
        numbers (List[float]): A list of numbers
        threshold (float): A threshold value
    Returns:
        bool: A flag indicating if all pairs of elements in the list are closer than the threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] <= threshold:
                return False
    return True
```

This script implements a helper function `any_two_are_close` that checks if all pairs of elements in the list are closer than the given threshold. The function iterates over all possible pairs of elements in the list and checks if their difference is less than or equal to the threshold.

Finally, the `has_close_elements` function is implemented by calling the `any_two_are_close` function with the list of numbers and the threshold as arguments.