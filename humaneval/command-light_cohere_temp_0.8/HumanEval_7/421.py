```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

# Function call and test results
print(filter_by_substring(strings, substring))  # ['abc', 'bacd', 'array']

strings2 = ["123", "abc", "hello"]
substring2 = "123"

# Function call and test results
print(filter_by_substring(strings2, substring2))  # []
``` 
This script defines a function `filter_by_substring` that takes two arguments - a list of strings and a substring. It uses a `List[x for x in strings if substring in x]` to filter the list of strings, which contains only the strings that contain the given substring.