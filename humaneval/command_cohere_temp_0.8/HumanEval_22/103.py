```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
```

The function calls itself `filter_integers()` which takes in a list of values and returns a list of integers by filtering out any non-integer values. It utilizes the `isinstance()` function with an argument of `int` to check if each value in the list is an integer, and if so, it includes that value in the `integers` list which is returned at the end of the function. The function's description and docstring are also included to provide a description of its purpose and usage. 

This solution has a time complexity of `O(n)` as it linearly traverses the input list, and has a space complexity of `O(n)` as it creates a new list of integers. 

These complexity considerations may not be relevant for a small number of tests, but are considered for larger real-world datasets.