Here's the self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    return any(x < y for x, y in zip(numbers, numbers[1:])) and numbers[0] <= threshold
```
This function uses the Python **any()** function to check if there are any elements in the list that are less than the corresponding elements in the list and the threshold. The function returns True first element in the list that is less than the second element and returns **True**. If there are no such elements, it returns **False**.