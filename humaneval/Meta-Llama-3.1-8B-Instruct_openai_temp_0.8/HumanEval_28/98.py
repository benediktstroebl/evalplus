```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    
    Args:
        strings: A list of strings to be concatenated
    
    Returns:
        A single string resulting from concatenating the input list
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    return ''.join(strings)
```

You can run this script and test the function with different inputs to see its behavior. The `join()` method is a built-in string method in Python that returns a string concatenated with the elements of an iterable. In this case, we're passing the input list `strings` to `join()` to concatenate all strings in the list. If the input list is empty, `join()` would return an empty string.