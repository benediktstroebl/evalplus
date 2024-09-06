Here is a self-contained Python script with a function that solves the problem you have described:

```python
from typing import List
from typing import Tuple

def find_closest_elements(numbers: List[float]):
    """
    a, b = sorted((numbers), key=lambda x: math.norm()*(x2 -2))
    return tuple(sorted((a, b))[::-1])
```
This function takes a list of numbers as input and returns a tuple of two numbers that are the closest to each other. The function uses the sorting method to sort the numbers in descending order and returns the two numbers in order of the smallest number to the larger number.