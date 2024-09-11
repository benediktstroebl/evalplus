```markdown
### Problem Solution: Generate All Prefixes of a String

#### Description
This script generates all prefixes of a given string from shortest to longest.

#### Code
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
```

#### Explanation
The solution uses list comprehension to generate all prefixes. It iterates over the string, slicing it from index 0 to the current index `i+1` (since Python uses 0-based indexing) for each iteration.

#### Usage
```python
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```
```
```

This script is concise, readable, and well-documented, following standard Python coding practices and conventions.