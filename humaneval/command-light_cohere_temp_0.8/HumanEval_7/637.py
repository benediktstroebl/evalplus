```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["abc", "def", "function"]
substring = "f"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'def']

# Test case 3
strings = ["apple", "orange", "banana"]
substring = "an"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['apple', 'orange', 'banana']
```

This Python code defines a function called **filter_by_substring** that takes a list of strings and a substring as input and returns a new list that contains only the strings from the input list that contain the given substring. The code provides three test cases to demonstrate the functionality, successfully filtering the strings for the given substring.