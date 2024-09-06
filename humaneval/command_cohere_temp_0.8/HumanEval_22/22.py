```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type as input. It returns a list containing only the integer values from the input list. To achieve this, it uses a list comprehension that checks if each element in the input list is an instance of the int type, and if so, includes it in the result list. The function's type annotation specifies that it accepts a list of arbitrary values (`List[Any])` and returns a list of integers (`List[int]`).