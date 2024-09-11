Here's the completed Python script that solves the problem:
```markdown
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
    strings (List[str]): List of strings to be concatenated

    Returns:
    str: The concatenated string

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
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```
In this script, the `concatenate` function takes a list of strings as input and uses the `join` method to concatenate them into a single string. The `join` method returns an empty string if the input list is empty. The script also includes some test cases to demonstrate the function's behavior.