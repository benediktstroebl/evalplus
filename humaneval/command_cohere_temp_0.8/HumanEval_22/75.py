```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code provides an implementation of the `filter_integers` function, which takes in a list of values of any type and returns a list of integers from that list. It uses a list comprehension, which iterates over each value in the input list, and if the instance of each value is int (i.e., the value is an integer), it adds it to the resulting list. The output is a list of integers. 

This solution is efficient and will not change regardless of the input order since it uses iterating and filtering rather than indexing, which could be affected by the order of the elements.