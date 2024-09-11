```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the concatenation of all strings in the input list.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['hello', 'world']))  # 'helloworld'
```

This script uses Python's built-in `join()` method of the string class, which concatenates all the strings in the list into a single string. The `join()` method takes an iterable (in this case, a list of strings) and concatenates its elements into a single string, with the string on which the method is called (in this case, an empty string) serving as the separator.