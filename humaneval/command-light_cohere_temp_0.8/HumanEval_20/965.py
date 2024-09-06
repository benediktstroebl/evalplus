Here is a self-contained Python script that solves the problem:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    
    Parameters:
    numbers: List[float] - list of floating-point numbers to be compared
    
    Returns:
    Tuple[float, float] - A tuple containing the two numbers that are the closest to each other.
```

The script provides a function `find_closest_elements` that takes in a list of numbers and returns a tuple of the two numbers that are the closest to each other. The function uses the efficient algorithm provided by:

- The Manhattan Distance algorithm, which uses the `math.dist` function to calculate the minimum distance between two numbers in the list.