```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

#Test cases:
strings = ["abc", "bacd", "cde", "array", "Hello", "World"]
substrings = ["a", "bd", "cd"]

result = filter_by_substring(strings, substrings)
print(result == ['abc', "bacd", "array"])  # True
print(result == ['Hello'])           # False
print(result == ['World'])           # False
```
This script defines a function `filter_by_substring` that filters a list of strings for a given substring. It then passes this tests to this function and checks the results against the expected output.