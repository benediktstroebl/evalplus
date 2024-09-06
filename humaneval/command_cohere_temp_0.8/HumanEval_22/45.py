```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the `List[Any]` parameter. The function filters this list and returns a new list that contains only the integers present in the input list. It uses a list comprehension to iterate over each element `x` in the input `values` list and checks if `x` is an instance of the `int` class, if so, it includes `x` in the `result` list. Finally, the function returns the `result` list containing the filtered integers. 

This solution allows you to filter any given list of various python values (strings, numbers, dictionaries, etc.) and obtain a list of integers that are present in the list. 

The given example test cases demonstrate the functionality of the function appropriately.