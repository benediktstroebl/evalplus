Here's a self-contained Python script with a function that checks whether any two numbers in a given list are closer to each other than a given threshold:

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for x, y in zip(numbers, numbers[1:]):
        if abs(x - y) <= threshold:
            return True
    return False
```
The above function, `has_close_elements`, iterates over pairs of elements in the list of numbers and checks if the absolute difference between two numbers is less than or equal to the given threshold. 
The function returns `True` if any such condition is met, indicating that the numbers are close to each other, and returns `False` otherwise. 
The function uses the typing module to provide type hints for the function parameters and returns a boolean result.