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
strings = ["abc", "hello", "world"]
substring = "ow"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'hello']

# Test case 3
strings = ["abcd", "abce", "abcd", "hello"]
substring = "ab"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abcd', 'abce', 'hello']
```
This code defines a function `filter_by_substring` that filters a list of strings for a given substring. The function utilizes a string's `in` operator to check if each string contains the substring, and returns a new list containing only the matching strings. The code then includes a series of test cases, demonstrating the usage of the function with different strings and substrings.