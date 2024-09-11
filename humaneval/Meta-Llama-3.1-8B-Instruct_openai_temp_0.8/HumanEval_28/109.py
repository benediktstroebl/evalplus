```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
    strings (List[str]): A list of strings to be concatenated
    
    Returns:
    str: A single string that is the result of concatenating all strings in the input list
    
    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    
    # Use the join() method of the string class to concatenate all strings in the list
    # The join() method takes an iterable of strings and concatenates them with the string it's called on in between each pair of strings
    # Since we want the strings to be concatenated without any separator, we call join() on an empty string
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Should print ''
print(concatenate(['a', 'b', 'c']))  # Should print 'abc'
print(concatenate(['Hello','', 'World!']))  # Should print 'Hello World!'
```

This script defines a function `concatenate` that takes a list of strings and returns a single string that is the result of concatenating all strings in the list. It uses the `join()` method of the string class to concatenate the strings, and it provides some test cases at the end to demonstrate how the function works.