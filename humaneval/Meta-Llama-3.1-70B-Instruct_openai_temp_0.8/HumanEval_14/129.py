```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This script defines a function `all_prefixes` that takes a string as input and returns a list of all prefixes of the string, from shortest to longest. The function uses a list comprehension to generate the prefixes. The `string[:i+1]` expression slices the input string up to the `i+1`th character, where `i` ranges from 0 to the length of the string minus 1. The resulting list of prefixes is then returned.

You can run this script and test the `all_prefixes` function with different input strings to see its output.