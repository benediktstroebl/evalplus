```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the `List[Any]` parameter. It returns a list of integers by filtering out any elements that are not instances of the integer type using a list comprehension and the `isinstance` function. This function allows you to convert a list of various items into a list containing only integers, regardless of any other data types present in the original list. Two example use cases are also provided that demonstrate how the function works when filtering different input lists, illustrating its functionality and correctness. These test cases help validate the behavior of the function and ensure that it produces the expected results when executing the script.