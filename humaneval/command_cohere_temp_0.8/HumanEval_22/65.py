```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the type hint `List[Any]` and returns a list of integers. The function utilizes a list comprehension to iterate through each value in the input list, and checks if each value is an instance of the integer class using the `isinstance` function. If a value is an integer, it is included in the `result` list. The output of the function is the `result` list containing only the integer values from the input list, regardless of other data types present.

Here is an example usage of the above function:
```python
values = ['a', 3.14, 5, 'foo', 7, 2.5]
filtered_integers = filter_integers(values)
print(filtered_integers)
```

The output will be:
```
[5, 7]
```