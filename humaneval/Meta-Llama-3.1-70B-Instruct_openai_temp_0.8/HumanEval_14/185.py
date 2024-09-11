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

This script defines the `all_prefixes` function, which uses a list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression returns a substring of `string` from the beginning to the `i+1` index, effectively creating a prefix of the desired length. The `range(len(string))` iterator ensures that we generate prefixes of all lengths from 1 to the full length of the input string.