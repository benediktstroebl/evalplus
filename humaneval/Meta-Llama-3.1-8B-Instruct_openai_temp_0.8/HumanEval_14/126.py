```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of all prefixes in the input string, from shortest to longest.

    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Testing the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script defines the `all_prefixes` function, which takes a string as input and returns a list of all its prefixes, from the shortest to the longest. The function uses a list comprehension to generate the list of prefixes. The test cases at the end demonstrate how to use the function with different input strings.