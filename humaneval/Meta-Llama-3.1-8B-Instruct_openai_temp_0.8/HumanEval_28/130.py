```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: The concatenated string
    """
    return ''.join(strings)

# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello','', 'world']))  # Output: 'hello world'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string by joining all the input strings together using the `join` method of an empty string (`''`). The result is a concatenated string that includes any whitespace characters from the input list. The example usage demonstrates how to call the function with different input lists and print the resulting concatenated strings.