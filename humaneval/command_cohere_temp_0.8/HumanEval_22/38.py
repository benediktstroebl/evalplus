```python
from typing import List, Any

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

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out all elements that are not of type `int`. It uses a list comprehension that iterates through each value in the input list. If the current value is an integer, it is appended to the `integers` list. Finally, the function returns the `integers` list, which will only contain integers. 

Here is an example usage of the function and its expected output:
```python
>>> filter_integers(['a', 3.14, 5])
[5]
>>> filter_integers([1, 2, 3, 'abc', {}, []])
[1, 2, 3]
``` 

This approach utilizes type hints and the `isinstance()` function to ensure compatibility and efficient filtering of the values. Let me know if you would like me to explain any part of the solution or provide additional information!