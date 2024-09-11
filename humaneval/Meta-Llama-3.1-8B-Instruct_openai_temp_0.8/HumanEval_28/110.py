```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: A single string that is the concatenation of all strings in the input list

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method returns a string concatenated with the elements of an iterable
    return ''.join(strings)

# Test the function
print(concatenate([]))   # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This Python script defines a function `concatenate` that takes a list of strings as input and returns a single string that is the concatenation of all strings in the list. The function uses the built-in `join()` method to concatenate all strings in the list. The `join()` method is called on an empty string (`''`), which means it will concatenate all strings without any separator. The script also includes test cases to demonstrate the function's behavior.