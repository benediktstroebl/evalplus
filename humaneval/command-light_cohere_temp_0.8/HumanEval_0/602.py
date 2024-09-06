Here is a self-contained Python function that solves the problem of checking if any two elements in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] - numbers[j] < threshold:
                return True
    return False
```

This function uses two nested loops to iterate through every pair of numbers in the list. It compares each pair of numbers and checks if the difference is less than the threshold. The function returns True after the returns True, which means that any two numbers in the list were closer than the threshold.

This function provides a simple and efficient way to solve the problem of checking if any two elements in a list are close enough.