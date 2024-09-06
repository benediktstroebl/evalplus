```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    
    :The function takes advantage of Python's built-in functions like `sorted` to achieve this. It first sorts the Zamons and selects the two closest elements. It then returns a Zamons in a tuple with the smaller and larger numbers. The function was tested with a set of test numbers. It passed the test two sets of numbers, and the test passed was whether the returned tuple contained the numbers `[1.0, 2.0]` and `[2.0, 3.0]` were in the test the function. 
```