```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return "".join(strings)

# Test case 1: Empty list
assert concatenate([]) == ""

# Test case 2: Simple list
assert concatenate(['a', 'b', 'c']) == "abc"

# Test case 3: List of strings with a newline character
assert concatenate(['a', '\n', 'b', 'c']) == "abc\nbcc"
```

The above Python code defines a function called `concatenate` that takes a list of strings as input and returns the concatenated string by using the `join` method. It provides three list of test cases to validate the correctness of the `concatenate` function.