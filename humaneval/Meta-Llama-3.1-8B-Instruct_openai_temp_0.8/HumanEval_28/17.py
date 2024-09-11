### Concatenating a List of Strings into a Single String

Below is a self-contained Python script that solves the problem.

```markdown
### Python Script

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: The concatenated string.

    Example Use Cases:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

### Explanation

The `concatenate` function uses the `join()` method to concatenate all strings in the input list. The `join()` method takes an iterable of strings as an argument and returns a single string that is the concatenation of all the strings in the iterable. When no argument is specified, `join()` uses an empty string as the separator, effectively concatenating the strings without any separators.