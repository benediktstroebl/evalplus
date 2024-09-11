### Concatenate List of Strings
#### Problem
Given a list of strings, create a function that concatenates them into a single string.

#### Solution
```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to be concatenated.
    
    Returns:
        str: A single string that is the result of concatenating all strings in the input list.
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)
```

#### Explanation
This solution uses the built-in `join()` method of Python strings, which concatenates all elements in an iterable (like a list) into a single string. The `join()` method is applied to an empty string (`''`), which means that no separator is used between the concatenated strings.

#### Example Use Cases

```python
# Concatenate two strings
print(concatenate(['Hello, ', 'world!']))  # Outputs: "Hello, world!"

# Concatenate multiple strings
print(concatenate(['This','is','a','test.']))  # Outputs: "This is a test."

# Concatenate an empty list
print(concatenate([]))  # Outputs: ""
```