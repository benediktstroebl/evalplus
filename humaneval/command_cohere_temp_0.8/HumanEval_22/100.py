```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the `List[Any]` type annotation. Inside the function, it uses a list comprehension to iterate over each element `x` in the input `values` list and checks if the element is an instance of the `int` class, if it is, it includes `x` in the `result` list. Finally, the function returns the `result` list containing only the integers from the input list, resulting in a list of integers if all elements are integers, and an empty list if there are no integers in the input list.