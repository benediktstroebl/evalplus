```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases
strings = ["abc", "bacd", "cde", "array", " hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. The function iterates through each string in the list and checks if the given substring exists in the string.