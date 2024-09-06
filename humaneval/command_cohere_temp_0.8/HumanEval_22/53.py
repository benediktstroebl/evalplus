```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the `List[Any]` parameter. The function filters this list to include only the elements that are instances of the `int` type, specified in the return type `List[int]`. This filtering is performed using a list comprehension, which iterates through each element in the input list and checks if it's an instance of the `int` type, and the resulting filtered list only contains integers. This function efficiently solves the problem and provides a clear and concise solution.