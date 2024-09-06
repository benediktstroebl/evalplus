Here is a self-contained Python function that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    """
    two numbers in numbers that are closer than or equal to the threshold, 
    return True
    """
    return any(abs(x - y) <= threshold for x, y in zip(numbers))

```

This function uses the `abs()` function to get the absolute value of each element in the list. Additionally, the `any()` function checks if any two elements in the list have a distance less than or equal to the threshold. The `return True` statement indicates that at least one pair of numbers in the list has a distance less than the threshold.

Please note that this function assumes that the input list contains only numeric values.