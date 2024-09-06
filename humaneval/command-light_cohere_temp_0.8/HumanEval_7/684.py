```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case #1: empty input list
print(filter_by_substring([], 'a'))  # Output: []

# Test case #2: containing the substring
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']

# Test case #3: not-of-the-substring
print(filter_by_substring(['abc', 'cdef', 'geeksforgeeks'], 'geeks'))  # Output: ['abc', 'cdef', 'geeks']
```

The provided function `filter_by_substring` is designed to filter an input list of strings and return a new list that includes only the strings containing the given substring.  The using the specific cases, you can further test the function with various inputs and expected outputs.