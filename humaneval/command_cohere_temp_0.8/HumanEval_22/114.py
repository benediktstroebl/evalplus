```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

The function calls the built-in `isinstance()` function, which checks if each list item has a type of `int`. The resulting list of such items is then returned. The function works for lists containing other data types like strings, floats, dictionaries, or arrays, as demonstrated in the given test examples. 
```python
def test_filter_integers():
    assert filter_integers(['a', 3.14, 5]) == [5]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
```

Note that the function includes type annotations and a docstring, which are best practices to improve code readability and maintainability.