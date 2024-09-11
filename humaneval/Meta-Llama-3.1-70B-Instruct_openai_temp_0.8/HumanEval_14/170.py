```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
This script defines the function `all_prefixes` that uses list comprehension to generate all prefixes of the input string. The `range(len(string))` generates indices from 0 to the length of the string minus 1, and `string[:i+1]` gets the substring from the start to the current index plus one (to include the character at the current index). The resulting list of prefixes is then returned.