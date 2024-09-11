```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of prefixes

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('abcdefg'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a list comprehension to generate the prefixes by slicing the input string with `[:i+1]` for each position `i` from 0 to the length of the string. The test cases demonstrate the function's behavior with different input strings.