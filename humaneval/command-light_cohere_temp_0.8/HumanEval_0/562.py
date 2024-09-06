Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    def check_close(a: float, b: float) -> bool:
        return a + b > threshold

    return any(check_close(num1, num2) for num1, num2 in zip(numbers))
```

This function checks if any two elements in the list are closer to each other than the given threshold. 
The `check_close` function compares the two elements, and returns `True` if they are closer than the threshold. 
The `has_close_elements` function uses the `any` function to check if any of the elements in the list satisfy this condition.