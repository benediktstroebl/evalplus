```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes in order from shortest to longest

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('a'))  # Output: ['a']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string in order from shortest to longest. It uses a list comprehension to generate the list of prefixes. The list comprehension iterates over the indices `i` in the range from 1 to the length of the input string, and for each index, it includes the substring of the input string from the start to that index. The `range(1, len(string) + 1)` ensures that we start from the shortest prefix ('a') and end at the longest prefix (the entire string).