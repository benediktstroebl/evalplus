Here is a self-contained Python script that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   occurs if the are two numbers that are less than the threshold.
    then, they are considered as close and the return true
    """
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] <= threshold:
                return True
    return False
```

The script defines a function `has_close_elements` that takes in two arguments: a list of numbers and a threshold. The function loops through the numbers, and for every pair of numbers, it checks if they are closer than the threshold. If the condition is met, the function returns `True`, and if it is false, it returns `False`.