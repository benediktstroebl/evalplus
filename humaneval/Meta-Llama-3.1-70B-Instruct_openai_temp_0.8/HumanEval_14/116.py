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
if __name__ == "__main__":
    print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
    print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that uses a list comprehension to generate all prefixes of the input string. The list comprehension iterates over the range of lengths from 1 to the length of the input string (inclusive), and for each length `i`, it slices the input string to get the prefix of that length. The resulting list of prefixes is then returned by the function.

The script also includes example usage in the `if __name__ == "__main__":` block, which demonstrates how to use the `all_prefixes` function with different input strings.