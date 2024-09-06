```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the `List[Any]` type annotation. The function filters this list and returns a new list that contains only the integer values from the original list. It does so by using a list comprehension that checks if each value in the `values` list is an instance of the `int` class, and if so, includes it in the `result` list. The resulting `result` list is then returned, providing a filtered list containing only the integer items from the input list. 

The function is designed to be self-contained, meaning it does not rely on any external variables or contexts; it cleanly encapsulates the filtering logic within itself.