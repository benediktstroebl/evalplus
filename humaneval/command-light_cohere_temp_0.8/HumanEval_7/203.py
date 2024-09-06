```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function:
strings = ['abc', 'bacd', 'cde', 'array', '105']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Expected output: ['abc', 'bacd', 'array']
```
This script provides a function `filter_by_substring` that filters a list of strings for a given substring.  It uses a one item from the input list and the substring to test. The function uses a list comprehension and returns a new list containing all items from the original list that contain the given substring.