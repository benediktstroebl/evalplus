```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
    strings (List[str]): A list of strings to be concatenated.

    Returns:
    str: A single string resulting from the concatenation of all strings in the input list.
    """
    # Use the join() method of an empty string to concatenate all strings in the list
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines the `concatenate` function, which takes a list of strings as input and returns their concatenation. The function uses the `join()` method of an empty string, which concatenates all elements in the input list into a single string. The script also includes test cases to demonstrate the function's behavior.