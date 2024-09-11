```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the result of concatenating all the input strings.

    Example:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    # The join() method returns a string that is the concatenation of all the strings in the list
    # We pass an empty string '' as the separator to the join() method
    return ''.join(strings)


# Test the function
if __name__ == '__main__':
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello','', 'World']))  # Output: 'Hello World'
```

In this script, the `concatenate` function takes a list of strings as input and uses the `join` method to concatenate them into a single string. The `join` method is applied to an empty string, which means it will use an empty string as the separator between the input strings. This results in a single string that is the concatenation of all the input strings. The script also includes some test cases to verify that the function works as expected.