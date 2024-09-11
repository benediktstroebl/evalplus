```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes an input string and returns a list of all its prefixes, from the shortest to the longest. The function uses a list comprehension to generate the prefixes.

Here's how it works:

- `string[:i+1]` is used to get the prefix of the string up to the `i-th` character.
- `range(len(string))` generates indices from 0 to the length of the string minus one.
- The list comprehension iterates over these indices, generates the corresponding prefixes, and stores them in a list.

The test at the end of the script demonstrates the function's correctness by printing the prefixes of the string `'abc'`.