Here's the solution to the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Returns the two closest elements in the list, and their order.
    Return the closest pair of numbers as a tuple.
    """return sorted([num1, num2], key=lambda a: math.abs(a))[:2][::-1]
```
This function takes a list of numbers and returns a tuple containing the two closest elements in the list, along with their order. The function sorts the two closest numbers to each other using the math.abs() function to ensure the absolute value, and then uses the sorted list to return the first two elements in the tuple.

The solution has been divided into a function and can be used to solve the problem easily.