```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

result = filter_by_substring(strings, substring)
print("Test case 1: ", end=" ")
print(result)  # Output: ['abc', 'bacd', 'array']

strings = ["abracdc"]
substring = "dc"

result = filter_by_substring(strings, substring)
print("\nTest case 2: ", end=" ")
print(result)  # Output: ['abracdc']

strings = ["abc", "foo", "bar", " Baz"]
substring = "abc"

result = filter_by_substring(strings, substring)
print("\nTest case 3: ", end=" ")
print(result)  # Output: ['abc']
```
This script defines a function `filter_by_substring` that filters a list of strings for a given substring. It uses the plain Python list comprehension to achieve this. You can use this different code block to call this function with your list of strings and substring, and then print the result.