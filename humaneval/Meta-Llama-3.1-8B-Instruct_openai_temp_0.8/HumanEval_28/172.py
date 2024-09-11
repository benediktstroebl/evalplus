```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated
    
    Returns:
        str: A single string containing all the elements from the input list
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

In this script, we define a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all the strings in the input list. The `join` method of the string class is used to concatenate the strings. The function is also tested with some example inputs to demonstrate its usage.