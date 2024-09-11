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
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all its prefixes in order from shortest to longest. The `[:i+1]` part of the list comprehension is used to get the substring from the start of the string up to index `i+1`, effectively getting the prefix of length `i+1`. The `range(len(string))` part generates the indices `i` to iterate over.