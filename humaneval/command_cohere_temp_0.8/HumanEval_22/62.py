```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

This function uses a list comprehension, which is a concise way to create a new list based on existing lists, to filter out items that are not integers. For each item in the input list, it checks if the item is an instance of int using the `isinstance()` function. If it is, it includes the item in the `int_list` buffer. Finally, the function returns the `int_list` buffer, which will contain only the integers from the original input list. 

Here is an example of how to use the function:
```python
values = ['a', 3.14, 5, 'foo', 7, 2.5]
result = filter_integers(values)
print(result)
```

And below are the corresponding test cases:
```python
def test_filter_integers():
    # Single integer case
    assert filter_integers([4]) == [4]

    # Mixed types case
    assert filter_integers([1, 'abc', 3, True, None, 7]) == [1, 3, 7]

    # Only non-integer case
    assert filter_integers([1.5, 'foo', ['foo']]) == []
```

This way, the `filter_integers()` function can successfully filter a list of varying values, ensuring that only integers pass through the filter, and this is achieved in a concise and efficient manner.  If you have any questions, let me know!