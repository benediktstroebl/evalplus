```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
    string (str): The input string.
    
    Returns:
    List[str]: A list of all prefixes of the input string.
    """
    return [string[:i] for i in range(1, len(string) + 1)]


# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']

# Test cases:
assert all_prefixes('') == []
assert all_prefixes('a') == ['a']
assert all_prefixes('abc') == ['a', 'ab', 'abc']
assert all_prefixes('abcdef') == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
```