```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.
    
    Args:
        string (str): The input string for which all prefixes are calculated.
    
    Returns:
        List[str]: A list of all prefixes in the input string, sorted from shortest to longest.
    
    Examples:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(1, len(string) + 1)]

# Example usage:
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```

In this code, we use a list comprehension to generate all prefixes. The expression `string[:i]` returns a substring of `string` starting from the beginning and ending at index `i`. The `range(1, len(string) + 1)` specifies the indices `i` that we want to use to generate the prefixes. The resulting list of prefixes is then returned.