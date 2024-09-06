```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

The function uses a list comprehension that iterates over each item in the input list values. The condition `isinstance(item, int)` checks if each item is an instance of the int class, meaning it is an integer, and filters these items into the int_list. After filtering, the function returns the int_list containing only the integer values from the input list.

Here is an example of use for the function:
```python
values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
print(filter_integers(values))
```

And below is the corresponding markdown code block:
```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """

# Tests
values = ['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
assert filter_integers(values) == [5, 1, 2, 3]
values = [1, 2, 3, 'abc', {}, []]
assert filter_integers(values) == [1, 2, 3]
```