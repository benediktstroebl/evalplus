Here is a self-contained Python script that solves the problem:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Return the two closest elements from the list and their order.
    """
    closest1 = min(numbers[0], numbers[1])
    2nd_closest = max(numbers[0], numbers[1])
    return (closest1, second_closest)
```
This function takes a list of numbers and returns a tuple containing the two closest elements in the list, along with their order.

The function uses the `min()` and `max()` functions on the list elements to find the two closest elements. 

Finally, the function returns the two values in tuple format, which are the two closest elements in the list.