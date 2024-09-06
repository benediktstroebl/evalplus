```python
def sort_third(lst):
    """Sorts the list l such that values divisible by three are in their correct positions, and the rest are in their original positions.
    Args:
        lst (list) : list of integers
    Returns:
        list: sorted list with values divisible by three in their correct positions and others in their original positions.
    """
from bisect import bisect_left
    lst = sorted(lst)
    index = bisect_left(lst, 3)
    lst = lst[:index] + [3] * index + lst[index:]
    return lst
```
This function utilizes the 'bisect_left' function from the 'bisect' module to identify the position of the third element.