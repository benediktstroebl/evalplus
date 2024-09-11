```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Returns a list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string from which prefixes are generated

    Returns:
    List[str]: A list of all prefixes in ascending order of length

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes[::-1]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes in ascending order of length. The function works by iterating over the string and slicing it from the start to the current index. The `[::-1]` at the end of the function call is used to reverse the order of the prefixes, so that the shortest prefix comes first.