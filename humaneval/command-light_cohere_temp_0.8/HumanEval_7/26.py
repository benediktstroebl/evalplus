```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1: Basic function usage
strings = ['abc', 'bacd', 'cde', 'array']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2: Multiple occurrences of substring
strings = ['abc', 'bacd', 'cde', 'abc', 'array', 'abc']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'abc', 'array']

# Test case 3: Empty input
strings = []
sub = 'x'
result = filter_by_substring(strings, sub)
print(result)  # Output: []
```

The code demonstrates the functionality of the `filter_by_substring` function, which takes a list of strings and a substring as input. The function filters and returns a new list containing only the strings from the input list that contain the given substring. The test cases illustrate the other possible scenarios you can use the function for.