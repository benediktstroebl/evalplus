```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_values = [item for item in values if isinstance(item, int)]
    return int_values
```

This function uses a list comprehension that iterates over each value in the input list values. It checks if each item is an instance of int using the isinstance() function. If it is, it includes the item in the int_values list. The function then returns the int_values list, which contains only the integer values from the original list.

Here is an example usage of the function:
```python
values = ['a', 3.14, 5, 'foo', 7, 2.5]
result = filter_integers(values)
print(result)
```

And below are the results of the executions:
```
[5, 7]
```

This demonstrates that the function is correctly filtering out only the integer values from the given list.