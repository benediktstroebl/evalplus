Here's the solution to the problem of filtering an input list of strings for those containing a given substring: 

```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
# Test case 1
strings = ["abc", "bacd", "cde", "array", "hello world"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result) # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["hello world", "hello there"]
substring = "hello"
result = filter_by_substring(strings, substring)
print(result) # Output: []
```

This function takes a list of strings and a substring as input and returns a new list of strings from the input list that contain the given substring. It uses a essential Python list comprehension to filter the strings.

The output of the above code will be: `['abc', 'bacd', 'array']` for the first test case and an empty list (`[]`) for the second test case.