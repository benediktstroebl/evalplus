```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): List of strings to be concatenated

    Returns:
    str: A single string that is the concatenation of all input strings
    """
    if not strings:  # check if the list is empty
        return ''
    return ''.join(strings)

# Test cases
if __name__ == '__main__':
    print(concatenate([]))  # ''
    print(concatenate(['a', 'b', 'c']))  # 'abc'
    print(concatenate(['Hello','', 'World']))  # 'Hello World'
    print(concatenate(['This','is','a','test']))  # 'This is a test'
```

In this script, the `concatenate` function uses the `''.join(strings)` method to concatenate all the strings in the input list into a single string. This is a more efficient and Pythonic way of concatenating strings compared to using the `+` operator. The test cases at the end demonstrate the function's behavior with different input lists.