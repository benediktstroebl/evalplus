```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This Python script uses a list comprehension to generate all prefixes of the input string. The `string[:i]` expression is used to get the substring from the start of the string up to but not including the `i-th` character. The `range(1, len(string) + 1)` generates indices from 1 to the length of the string, allowing us to get all prefixes from the shortest (1 character) to the longest (the entire string).