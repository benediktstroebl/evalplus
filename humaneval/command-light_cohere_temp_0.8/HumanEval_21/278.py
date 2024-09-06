Here's a self-contained Python script that solves the problem of scaling numbers within a given list:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers.sort(reverse())[::-1]
    numbers = [x / 100.0 for x in numbers]
    return numbers
```

This function takes a list of numbers as input and returns a new list with the numbers scaled to the range [0, 1]. The function achieves this by using list slicing with a negative step to reverse the sorting of the list, and then dividing each number by 100. The function then returns the result.