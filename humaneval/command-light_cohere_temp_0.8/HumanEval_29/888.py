```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [string for string in strings if string.startswith(prefix)]


# Testing the function
strings = ['abc', 'bcd', 'cde', 'array', 'abcn', 'bd']
prefix = 'ab'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```
This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a filtered list of strings that start with the given prefix. The testing section shows how the string values are provided, along with the corresponding desired prefix ('ab'), and the output of the function is displayed, which should match the expected output.