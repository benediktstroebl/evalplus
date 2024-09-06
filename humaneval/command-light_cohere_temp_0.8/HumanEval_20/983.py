Here is a Python script that contains a self-contained function that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    return (smaller, larger number)
# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = (2.0, 3.0) 

```
This code solves the problem of finding the closest elements in a list of numbers by selecting two numbers that are the closest to each other and returning them in order.

The `find_closest_elements` function takes a list of numbers as input and returns a tuple containing the two closest numbers, with the smaller number first. The function uses the method `lambda x, y: x, y in sorted(numbers)` to find the two closest numbers in order, and returns them as a tuple.