```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the type hint `List[Any]` and returns a list of integers. The function utilizes a list comprehension to iterate through each value in the input list, and checks if each value is an instance of the integer class using the `isinstance` function with the argument `int`. If a value is an integer, it is included in the `result` list. Finally, the function returns the `result` list containing only the integer values from the input list.