```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```