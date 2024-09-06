```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_values = [item for item in values if isinstance(item, int)]
    return int_values
```

The function calls the built-in `isinstance()` function, which checks if each list item has a type of `int`. The `filter_integers()` function accepts a list of values of any type and returns a list that includes only the items that have a type of `int`. 

Here is an example usage of the function providing the simplest use case and one more complex adding more data types in the list:
```python
filter_integers([1, 2, 3, 5, 6]) # [1, 2, 3, 5, 6]

filter_integers(['a', 3.14, 5, 'foo', 7.3, 2, {'some_dict': 42}, [1, 2]]) # [5, 2, 7, {'some_dict': 42}, [1, 2]]
``` 

The first example demonstrates a list containing only integers that will pass through the function without any changes. While the second example shows a list containing integers and other data types, and the function returns a list with only the integer values.