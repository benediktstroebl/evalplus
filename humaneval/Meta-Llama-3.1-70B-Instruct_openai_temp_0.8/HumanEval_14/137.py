```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the input string, ranging from the shortest to the longest. The list comprehension `[string[:i+1] for i in range(len(string))]` generates all prefixes by slicing the input string from the beginning to each position `i+1` in the string.

Note that the `+1` is necessary because Python's slicing operation is exclusive of the end index, so `string[:i]` would yield a prefix one character shorter than desired. The `range(len(string))` generates indices from `0` to `len(string)-1`, which are used as the end indices for the slicing operation.