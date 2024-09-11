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
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

In this script, we use a list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression gets all characters up to the current index `i` (inclusive). The `range(len(string))` generates indices from 0 to the length of the string minus 1, making sure we cover all possible prefixes.