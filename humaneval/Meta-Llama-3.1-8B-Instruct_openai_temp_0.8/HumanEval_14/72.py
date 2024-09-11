```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('abcde'))  # ['a', 'ab', 'abc', 'abcd', 'abcde']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from the shortest to the longest. It uses a for loop to iterate over the string from the first character to the last, appending each prefix to the `prefixes` list. The function finally returns the list of prefixes. The script also includes example use cases to demonstrate the function's behavior.