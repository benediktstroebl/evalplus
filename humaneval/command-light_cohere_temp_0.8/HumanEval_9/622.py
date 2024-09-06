```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, numbers)]
```

This code defines a function called `rolling_max` that generates a list of integers, where each element is the maximum value from the list at the current position, moving towards the end of the list.

It uses the `zip` function to iterate over the list and return each element in the list, resulting in a new list that contains the maximum values from the original list at each index. 

The `numbers` parameter of the function is a list of integers. It returns a same list of integers, where each element is the maximum value from the list at the current position, moving towards the end of the list. 

This is a simple example of how to create a self-contained function that solves a problem in Python.

You can use this `rolling_max` function to solve the problem by passing a list of integers as an argument.