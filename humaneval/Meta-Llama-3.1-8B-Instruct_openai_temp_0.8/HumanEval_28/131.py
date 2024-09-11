### Concatenate List of Strings into a Single String
#### Problem Description

This Python script defines a function `concatenate` that takes a list of strings as input and returns a single string formed by concatenating all the input strings.

#### Solution

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: A single string formed by concatenating all the input strings

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```

#### Explanation

*   We use the built-in `join` function in Python, which concatenates all the strings in a list into a single string.
*   The `join` function takes an iterable (in this case, a list of strings) and concatenates its elements into a single string.
*   Since we're concatenating strings, we use an empty string (`''`) as the separator, effectively concatenating the strings without any additional characters in between.
*   The function takes advantage of the fact that `join` returns an empty string if the input list is empty, thus satisfying the first example in the docstring.

This script is self-contained and includes all necessary code to define and test the `concatenate` function.