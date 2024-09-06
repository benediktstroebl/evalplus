Here is a self-contained Python script that solves the problem you've described:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Returns a tuple of the two closest elements in the list, and their order.
   
    # Sort the elements in ascending order
    elements = sorted(numbers)
    # Take the first two elements
    first, second = elements[:2]
    # Check which is smaller and which is larger
    if first < second:
        return (first, second)
    else:
        return (second, first)
```

This function takes a list of numbers as an input and returns a tuple containing the two elements that are the closest to each other in the list, in ascending order.

The function first sorts the list of numbers in ascending order. Then, it takes the first two elements from the sorted list and checks which is smaller and which is larger. Finally, it returns a corresponding tuple of the two elements.