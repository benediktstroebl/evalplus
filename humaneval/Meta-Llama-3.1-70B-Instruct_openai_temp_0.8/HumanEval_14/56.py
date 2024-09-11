```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Returns a list of all prefixes from shortest to longest of the input string.

    Args:
    string (str): The input string.

    Returns:
    List[str]: A list of prefixes.
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, the `all_prefixes` function uses a list comprehension to generate all prefixes of the input string. It does this by iterating over the indices of the string (from 0 to the length of the string minus 1), slicing the string up to the current index plus 1, and adding the resulting substring to the list of prefixes.