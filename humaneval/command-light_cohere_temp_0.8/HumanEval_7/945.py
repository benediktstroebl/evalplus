Here's the solution for the markdown code block:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]
```

# Test cases:
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the specified substring. 

The function uses a list comprehension to iterate through each string in the input list, and if a string contains the given substring, it is added to the `result` list. 

The test cases demonstrate how the function works, filtering the input list for the substring 'a'.