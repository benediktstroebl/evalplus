```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script uses a list comprehension to generate a list of prefixes from the input string. The range `range(1, len(string) + 1)` generates the indices from 1 to the length of the string, and `string[:i]` extracts the substring from the start of the string to the current index `i`. The result is a list of prefixes in order from shortest to longest.