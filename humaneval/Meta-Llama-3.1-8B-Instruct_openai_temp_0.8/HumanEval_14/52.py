```markdown
### Generate All Prefixes of a String
#### Problem Description
Given a string, return a list of all prefixes from shortest to longest.

#### Solution
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

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```
#### Explanation
This solution uses a list comprehension to generate all prefixes of the input string. It iterates over the indices of the string, slicing the string from the start to the current index (`string[:i+1]`). The result is a list of all prefixes from shortest to longest.
```