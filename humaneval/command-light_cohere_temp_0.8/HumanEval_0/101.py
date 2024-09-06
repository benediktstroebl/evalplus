```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers: list of float
    return any(map(lambda x,y: x!=threshold and y!=threshold and x+y<threshold,numbers)))
```
This function uses a map function with a lambda function to check if any element in the numbers list is not equal to the threshold, and not equal to itself. It also checks if the same element is greater than the threshold, which will return true as well.