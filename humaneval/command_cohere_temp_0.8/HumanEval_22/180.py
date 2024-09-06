```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code directly uses a list comprehension to filter out elements that are not of type `int`. The use of the `isinstance()` function ensures that the elements are checked for their type and only convert to integers if they are indeed integers.