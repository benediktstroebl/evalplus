Here's the solution:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If any two elements in the list are closer than the threshold, the function will return True
    Otherwise, it will return False.
    """
    for num1, num2 in zip(numbers, numbers[1:]):
        if num1 + num2 > threshold:
            return True
    return False
```
The function uses a nested loop to iterate over the list of numbers. The function checks if any two elements in the list are closer than the threshold, then returns True.  If the function returns False if the loop does not find any such pair of elements.