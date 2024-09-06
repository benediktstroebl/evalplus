```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code directly uses a list comprehension to produce a list of integers from the input list. The `isinstance()` function is used to determine if each element in the input list is an instance of the integer class, which is used to filter out non-integer elements.