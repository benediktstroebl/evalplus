```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out all elements that are not of type `int`. It uses list comprehension to filter out non-integer values and returns a list that only contains the integers from the original list. 

Here's an example usage of the function:
```python
values = ['a', 3.14, 5, 'foo', 7.5, 2.99, 4]
result = filter_integers(values)
print(result)
```

And below is the expected output for the example:
```python
[5, 7, 4]
```