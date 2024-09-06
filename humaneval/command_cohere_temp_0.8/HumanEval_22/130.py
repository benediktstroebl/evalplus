```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The function uses a list comprehension, which is a concise way to create a new list by applying a transformation to each item in an existing list. Here, the transformation is filtering out values that are not integers. 

This solution relies on the `isinstance()` function, which returns True when the provided object is an instance of the class or type specified as the argument. In this case, the function checks if each element of the input list is an instance of the integer class, which is denoted by the `int` type. 

To see it in action, you can call the function with various input lists and see it return a new list containing only the integers present in the input.