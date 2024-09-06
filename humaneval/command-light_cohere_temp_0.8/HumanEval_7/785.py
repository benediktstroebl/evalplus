Here is a Python script that contains a self-contained function that filters an input list of strings based on a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings, returning those that contain the given substring."""
    return [s for s in strings if substring in s]

# Test the function with a few examples
strings = ['abc', 'bacd', 'cde', 'array', 'xares']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)
```

This script defines a function `filter_by_substring` that takes two arguments: a list of strings `strings` and a substring `substring`. It uses a list comprehension to iterate through the input strings, checking if each string contains the given substring. 

The script then tests the function with an example, printing the result, which should be the list of strings from the input list that contain the given substring.