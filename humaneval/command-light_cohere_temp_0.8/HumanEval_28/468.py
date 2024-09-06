```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return "".join(strings)

# Test the function with various inputs
strings_list = ["a", "b", "c", "d"]
print(concatenate(strings_list))  # Output: abcdd

long_string = "This is a very long string for testing purposes..."
print(concatenate([long_string]))  # Output: ThisisahcmVlongstringfortesting

# purposes
```