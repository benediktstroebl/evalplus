Here is a Python script that contains a self-contained function that solves the problem of finding the closest elements in a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two that are the closest to each other and return them in order (smaller number, larger number).
    
    Parameters:
        numbers: List[float] - list of floating-point numbers
        
    Returns:
        Tuple[float, float] - two numbers that are closest to each other and in order of the total value
    """
    a,b = sorted((numbers[::2], numbers[1::2]), key= lambda x: x[0]*x[1])
    return a,b
```

The function `find_closest_elements` takes a list of numbers and returns a tuple of two closest numbers. The function uses the methods `sorted()` and `key` to select the two closest numbers. The `key` parameter specifies that the lambda function should be applied to the product of the elements at the 0th and 1 positions in each sublist.

This function follows the format of a functional programming paradigm and is self-contained, meaning it does not require any external variables or functions to solve the problem.