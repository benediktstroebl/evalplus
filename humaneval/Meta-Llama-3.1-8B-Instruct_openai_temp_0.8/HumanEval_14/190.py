```markdown
### Solution for Problem: All Prefixes of a String

#### Problem Statement
Given a string, return a list of all prefixes from shortest to longest.

#### Code
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    Args:
        string (str): Input string

    Returns:
        List[str]: List of prefixes

    Example:
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]
```

#### Explanation
This function uses a list comprehension to generate all prefixes. The expression `string[:i+1]` returns a slice of the input string from the start to the `i-th` index (inclusive). The `range(len(string))` function generates numbers from 0 to the length of the string (exclusive).

#### Example Usage
```python
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```