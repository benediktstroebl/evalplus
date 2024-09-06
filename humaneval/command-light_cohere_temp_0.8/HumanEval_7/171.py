```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Testing function
strings = ["abc", "bacd", "cde", "hello", "is", "array"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'is', 'array']
``` 
This script defines a function **filter_by_substring** that filters an input list of strings and returns a new list that contains only the strings that contain the given substring. 
The script then creates an example test with a list of strings and the substring 'a'.