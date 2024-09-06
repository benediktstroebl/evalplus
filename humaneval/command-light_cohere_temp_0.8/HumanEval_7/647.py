```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output ['abc', 'bacd', 'array']
```
This code defines a function called **filter_by_substring** that takes two arguments: a list of strings and a substring. It uses the filter method to iterate over the list of strings and return only those that contain the given substring. The output will be the strings that contain the substring **'a'** in them, which are 'abc', 'bacd', and 'array'.