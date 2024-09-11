```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes from shortest to longest.

    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

In this script, the function `all_prefixes` uses list comprehension to generate all prefixes of the input string. It iterates over the indices of the string (from 0 to the length of the string minus 1), slices the string up to each index plus one (to include the character at the index), and includes the resulting prefix in the output list.

You can run this script in your Python environment to see the result.