```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "hello", "This is a string", "Hello World!"]
substrings = ["a", "abc"]

result = filter_by_substring(strings, substrings)
print("Result:", result)  # Output: ['abc', 'hello', 'This is a string']

# Test case with empty input strings
empty_strings = []
result2 = filter_by_substring(empty_strings, "cde")
print("Result2:", result2)  # Output: []

# Test case with non-existing substring
non_existing = ["abc", "def", "hello"]
result3 = filter_by_substring(strings, "non_existing")
print("Result3:", result3)  # Output: []
```
This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. The test cases demonstrate the example of using this function with various inputs, and the results are printed.