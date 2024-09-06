```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code provides a function to filter out integers from a list of python values. The function uses a list comprehension to check if each element in the provided list is an instance of the integer class, and returns a new list with those elements that are integers. As the function result is auto-documented by the type hinting, it provides a clear view of what the function returns.