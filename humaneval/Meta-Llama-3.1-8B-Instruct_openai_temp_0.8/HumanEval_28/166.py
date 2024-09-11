### Concatenating a List of Strings in Python
#### Using the `join()` Method

Here's a simple Python function that uses the `join()` method to concatenate a list of strings into a single string:

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): List of strings to be concatenated.

    Returns:
        str: Concatenated string.

    Example:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Example usage:
print(concatenate(['Hello','', 'World!']))  # Output: "Hello World!"
print(concatenate(['apple', 'banana', 'cherry']))  # Output: "applebananacherry"
print(concatenate([]))  # Output: ""
```

In this script, we define a function `concatenate` that takes a list of strings as input and returns a single string by joining all the strings in the list using the `join()` method. The `join()` method concatenates all the strings in the list into a single string, with the string it's called on as the separator. In this case, we use an empty string (`''`) as the separator, effectively concatenating the strings without any spaces in between.