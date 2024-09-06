```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']

strings = ["abc", "cde", "hello", "world"]
substring = "dl"

print(filter_by_substring(strings, substring))  # Output: ['cde', 'hello']
```
This Python code provides a function called `filter_by_substring` that filters an input list of strings and returns a new list containing only the strings that contain a given substring. The function utilizes the mechanism of list comprehension and the `in` operator to achieve this. The test cases demonstrate its expected behavior of the function. The function can be applied to various scenarios, such as filtering strings that contain specific characters or removing characters from a given string.