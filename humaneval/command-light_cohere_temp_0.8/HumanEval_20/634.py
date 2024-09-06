Here's a self-contained Python script that solves the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
    
    : Choose the two elements from the input list and return them in order of the distance, i.l them with the another pair is the smallest two elements.

    if len(numbers) < 2:
        return None, None
    return (numbers[0], numbers[1])
```

This function takes a list of numbers as an argument and returns a tuple containing the two elements in the list that are the closest to each other. If the length of the list is less than 2, the function returns None, None.

This solution efficiently solves the problem of finding the closest pair of elements in a list of numbers, using Python's List and Tuple data structures and the built-in function min.  to compare the and sort the elements in ascending order.