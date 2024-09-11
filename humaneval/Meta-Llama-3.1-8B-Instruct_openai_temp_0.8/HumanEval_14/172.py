### All Prefixes of a String
#### Python Script

```markdown
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    
    Args:
    string (str): The input string.
    
    Returns:
    List[str]: A list of all prefixes of the input string, from shortest to longest.
    
    Example:
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]
```

This script uses a list comprehension to generate all prefixes of the input string. The `string[:i+1]` expression slices the string from the start up to index `i+1`, effectively creating a prefix of length `i+1`. The `range(len(string))` generates a sequence of indices from `0` to `len(string)-1`, and the list comprehension creates a list of all prefixes for each index. The resulting list is then returned by the function.

You can use this script as follows:
```python
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
```