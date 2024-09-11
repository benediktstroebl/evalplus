```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This function uses list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression creates a substring from the beginning of the string to the current index `i+1`, effectively creating a prefix. The `range(len(string))` generates indices from 0 to the length of the string, excluding the length itself. The resulting list of prefixes is returned by the function.