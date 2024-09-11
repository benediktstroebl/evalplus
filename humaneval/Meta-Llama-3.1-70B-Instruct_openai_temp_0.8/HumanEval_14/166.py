```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script works by using a list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression slices the string from the beginning up to the `i+1`th character, which effectively generates all prefixes of lengths from 1 to the length of the string.