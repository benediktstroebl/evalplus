```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Testing the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes(''))  # Output: []
```

In this script, we use a list comprehension to generate all prefixes of the input string. The `range(len(string))` generates indices from 0 to the length of the string minus 1, and `string[:i+1]` generates the substring from the start of the string to the current index `i+1`. This way, we get all prefixes from the shortest to the longest.