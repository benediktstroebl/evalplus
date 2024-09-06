Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(x == y for x, y in zip(numbers, numbers[1:])) and numbers[0] < threshold
```
The above code will return a boolean value, which indicates whether any two numbers in the list are closer to each other than the given threshold. The function uses the shallow comparison (`==`) to check if any two numbers in the list are equal to each other, and then checks if the first number in the list is less than the given threshold.