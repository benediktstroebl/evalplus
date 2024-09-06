```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
test_filter = [lambda: filter_by_substring(strings, substring) != ['abc', 'bacd', "array"],]
test_not_substring = [lambda: filter_by_substring(strings, "cd") != strings]
test_empty = [lambda: filter_by_substring([], substring)]
test_not_empty = [lambda: filter_by_substring(strings, substring) != strings]
# Output:
print("Test Filter:", test_filter)
print("Test Not Substring:", test_not_substring)
print("Test Empty:", test_empty)
print("Test Not Empty:", test_not_empty)
```
The script defines a function `filter_by_substring` that filters an input list of strings to include only those that contain a given substring. It uses the certain list comprehension to check if the substring exists in each string, and returns a new list containing only the matching strings. The test cases demonstrate how the for different scenarios.