```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string

    Returns:
        List[str]: A list of all prefixes of the input string

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

In this script, we use a list comprehension to generate all prefixes of the input string. The `range(len(string))` generates numbers from 0 to the length of the string, and `string[:i+1]` generates a prefix of the string up to the current index `i`. The `+1` is used because string slicing in Python is exclusive of the end index, so we need to add 1 to include the last character in each prefix. The function returns a list of all these prefixes, ordered from shortest to longest.