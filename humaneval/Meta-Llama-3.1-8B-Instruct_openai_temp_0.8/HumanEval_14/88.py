```markdown
### Solution to Find All Prefixes of a String

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes from shortest to longest. The function uses a list comprehension with a generator expression to efficiently generate all prefixes.

#### Code

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

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
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```
#### Explanation

This code defines a function `all_prefixes` that takes a string `string` as input. It uses a list comprehension to generate all prefixes of the input string. The list comprehension iterates over the range of indices from 0 to the length of the string, and for each index `i`, it extracts the prefix of length `i+1` by slicing the string up to index `i+1` (since Python uses 0-based indexing). The resulting list of prefixes is then returned.

The test cases demonstrate the function's behavior on the input strings "abc" and "hello".