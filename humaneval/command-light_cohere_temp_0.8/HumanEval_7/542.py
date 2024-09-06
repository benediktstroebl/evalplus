```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """ 
    return [x for x in strings if substring in x]


# Test suite 

# Test 1
strings = ["abc", "bacd", "cde", "aa", "array"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'aa']

# Test 2
strings = ["abc", "bacd", "cde", "array", "x", "y"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'cde', 'array']

# Test 3
strings = ["abc", "def"]
substring = "def"
result = filter_by_substring(strings, substring)
print(result)  
# Output: []
```