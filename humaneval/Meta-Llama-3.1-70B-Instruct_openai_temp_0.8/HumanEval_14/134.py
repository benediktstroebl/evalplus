```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): The input string.

    Returns:
        List[str]: A list of all prefixes of the input string.
    """
    # Use list comprehension to generate all prefixes
    # The range starts from 1 because an empty string is not a prefix
    return [string[:i] for i in range(1, len(string) + 1)]


# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']

# Add more test cases
print(all_prefixes(''))  # Output: []
print(all_prefixes('a'))  # Output: ['a']
print(all_prefixes('abcd'))  # Output: ['a', 'ab', 'abc', 'abcd']
```