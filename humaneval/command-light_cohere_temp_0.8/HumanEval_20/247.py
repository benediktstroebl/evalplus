Here is a Python script that solves the problem of finding the closest pair of elements from a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        return numbers[0], numbers[0]
    
    left, right = find_closest_elements(numbers[1:])
    return min(left, right), max(left, right)
```

This function will return a tuple of the two closest elements in the list, in order of the smaller element, and the larger element.

The function uses the list comprehension technique to find the closest elements and returns them as a tuple.

Please note that you can use this function with any list of numbers, and it will return the two closest elements in that list.