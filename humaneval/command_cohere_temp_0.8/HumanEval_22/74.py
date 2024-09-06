```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the `List[Any]` type hint. Inside the function, it uses a list comprehension to iterate over each element `x` in the input `values` list and checks if the element is an instance of the `int` class, which represents integers. If it is an integer, it includes `x` in the `result` list. Finally, the function returns the `result` list, which contains only the integer values from the input list.