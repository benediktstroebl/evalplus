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

This script uses a list comprehension to generate all prefixes of the input string. The expression `string[:i+1]` generates a slice of the string from the start up to (but not including) the index `i+1`, effectively creating a prefix of length `i+1`. This is done for all indices `i` in the range from 0 to the length of the string minus 1, resulting in all prefixes from shortest to longest.