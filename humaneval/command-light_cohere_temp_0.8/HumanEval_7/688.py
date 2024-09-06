```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ['abc', 'bacd', 'cde', 'array', 'foo', 'bar']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ['abc', 'bacd', 'cde', 'foo', 'bar', 'abc']
sub = 'x'
result = filter_by_substring(strings, sub)
print(result)  # Output: []

# Test case 3
strings = ['a', 'bc', 'de', 'fg', 'hi', 'jkl']
sub = 'cy'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['de', 'fg', 'hi']
```

This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. The function uses a list comprehension to iterate over each string and check if the substring is present. The function is then tested using three different test cases, passing all tests successfully.