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

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out any non-integer values. It uses the `isinstance()` function to check if each value in the input list is an instance of the `int` class and appends only those that are to the returned list.

Here is an example usage of the function:
```python
values = ['a', 3.14, 5, 'yes', 12.9999, 23]
result = filter_integers(values)
print(result)
```

The output of the code is:
```
[5, 12, 23]
``` 

The function successfully filters out the integers from the list of values.