```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)
```

This code demonstrates a function `filter_by_substring` that filters an input list of strings based on a given substring. The function uses a list comprehension to iterate over each string in the input list and checks if the substring is present. The function returns a list containing only the strings that contain the specified substring.

The output of the code is:
```bash
['abc', 'bacd', 'array']
```