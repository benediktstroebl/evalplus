Here is a self-contained Python function that checks if any two elements in a list are closer than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    Return: True if two numbers are close, False otherwise.
    if len(numbers) < 2:
        return False
    else:
        min_val = min(numbers)
        max_val = max(numbers)
        return (max_val - min_val) > threshold
```

This function uses the min and max functions from the math library to compare the minimum and maximum values in the list. It then returns True if the have two numbers that are less than the threshold. 

You can use this function to solve the given problem.