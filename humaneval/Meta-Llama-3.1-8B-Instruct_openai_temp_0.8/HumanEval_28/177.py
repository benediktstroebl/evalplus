### Concatenate List of Strings into a Single String

Here's a Python script that defines a function `concatenate` to combine a list of strings into a single string.

```markdown
### Code

```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the concatenation of all input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


# Test the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

### Explanation

The `concatenate` function uses the built-in `join` method of the string class, which concatenates all the strings in the list and returns the result as a single string. If the input list is empty, an empty string is returned.

The script also includes some test cases to demonstrate the function's behavior. The `if __name__ == "__main__":` block is used to ensure that the test cases are only executed when the script is run directly, not when it's imported as a module.