```python
# Retrieve the string that joins the elements of the list
import string

def concatenate(strings: list) -> str:
    """
    Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated_string = string.join(strings)
    return concatenated_string
```

This code uses the `string.join()` method to join the elements of the list (`strings`) into a single string. The resulting concatenated string is then returned. 

The docstring includes example usage that outputs an empty string for an empty list and correctly joins the individual strings in the list when they are non-empty.