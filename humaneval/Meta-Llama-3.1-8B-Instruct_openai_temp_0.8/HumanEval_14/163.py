```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of prefixes of the input string

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

This script uses list comprehension to generate a list of all prefixes of the input string. It does this by slicing the string for each possible length from 1 to the length of the string. The `range(len(string))` generates numbers from 0 to the length of the string minus one, and `string[:i+1]` slices the string for each of these numbers. The `+1` is used to include the empty string (which is a prefix of any string) and the full string itself in the list of prefixes.