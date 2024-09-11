```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
    string (str): The input string

    Returns:
    List[str]: A list of all prefixes of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for length in range(1, len(string) + 1):
        prefix = string[:length]
        prefixes.append(prefix)
    return prefixes

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

In this script, the `all_prefixes` function works by iterating over the range from 1 to the length of the input string (inclusive). For each length, it creates a prefix of the string by slicing the string up to that length and appends it to the list of prefixes. Finally, it returns the list of prefixes.