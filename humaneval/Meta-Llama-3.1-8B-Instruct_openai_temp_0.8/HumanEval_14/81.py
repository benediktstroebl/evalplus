```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = [string[:i+1] for i in range(len(string))]
    return sorted(prefixes, key=len)

# Example usage
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('xyz'))  # Output: ['x', 'xy', 'xyz']
```

This script uses a list comprehension to generate all prefixes of the input string. It then uses the `sorted` function with the `key` argument set to `len` to sort the prefixes by length, from shortest to longest.