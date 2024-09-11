```python
from typing import List
import functools

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated.
    
    Returns:
        str: A single string resulting from concatenating all strings in the input list.
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use functools.reduce to concatenate all strings in the list
    return functools.reduce(lambda x, y: x + y, strings, '')

# Test the function
print(concatenate([]))  # Should print: ''
print(concatenate(['a', 'b', 'c']))  # Should print: 'abc'
```

In this code, `functools.reduce` is used to apply the `lambda` function to the first two elements of the list, then to the result and the next element, and so on, until only one element is left. The initial value of the accumulator is an empty string (`''`), so the function will work correctly even if the input list is empty.