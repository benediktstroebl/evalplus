```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
substrings = ["a", "World"]

result = filter_by_substring(strings, substrings)
print("For strings: ", strings)
print("Substrings:", substrings)
print("Filtered:", result)
```
This Python script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function works by iterating through each string in the list, checking if the given substring is present. The test cases below show how this function can correctly filter the strings based on the given substring.