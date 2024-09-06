Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # sort the list of numbers
    numbers.sort(key=lambda x: (-x, x))
    # find the first and second items of the sorted list
    first, second = numbers[0], numbers[-1]
    # check which number is larger, and return the other value
    if numbers[0] < first:
        return first, second
    elif numbers[-1] < second:
        return second, first
    else:
        return first, second
```
This function takes a list of numbers as input and returns a tuple of the two closest elements in the list.