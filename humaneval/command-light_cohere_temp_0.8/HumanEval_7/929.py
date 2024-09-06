```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
my_strings = ['abc', 'bacd', 'cde', 'array', 'hello']
my_substring = 'a'
result = filter_by_substring(my_strings, my_substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that takes two parameters: a list of strings and a substring. The function uses a list comprehension to filter the strings that contain the given substring, and the result is returned as a new list.