Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.lowercase(substring)]


# Example usage
my_strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
my_substring = 'a'
result = filter_by_substring(my_strings, my_substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that filters a list of strings for a given substring. The function uses a lower case of the substring to ensure that it matches properly.