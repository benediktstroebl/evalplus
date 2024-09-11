```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return list of all prefixes from shortest to longest of the input string.

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]


# Test the function
print(all_prefixes('abc'))  # Expected output: ['a', 'ab', 'abc']
print(all_prefixes(''))     # Expected output: []
print(all_prefixes('a'))    # Expected output: ['a']
```

In this script, we define a function `all_prefixes` that takes an input string and returns a list of all prefixes from shortest to longest. The function uses a list comprehension to generate the prefixes by slicing the input string from the start up to each index `i+1` in the range of the length of the string. The test cases at the end of the script verify that the function works correctly for different inputs.