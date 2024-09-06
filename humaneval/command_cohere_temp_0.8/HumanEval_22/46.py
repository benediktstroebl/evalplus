```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type as input. It uses a list comprehension to iterate through each value in the input list. For each value, it checks if the value is an instance of the integer class using the `isinstance` function with the argument `int`. If it is, the value is included in the `result` list. Finally, the function returns the `result` list, which contains only the integer values from the input list.