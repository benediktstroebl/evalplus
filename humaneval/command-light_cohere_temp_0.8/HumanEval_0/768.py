Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = sorted(numbers)
    for i in range(1, len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] - numbers[i] < threshold:
                return True
    return False


# Test the function with a sample input
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2, 6, 7, 8, 9]
result = has_close_elements(numbers, 0.8)
print(result)  # Output: True
```

This script defines a function called `has_close_elements` that takes a list of numbers and a threshold as input. It then sorts the numbers in ascending order and then checks if there are any two numbers that are closer than each other than the threshold. It returns `True` if any elements satisfy this condition.