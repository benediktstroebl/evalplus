```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

results = filter_by_substring(strings, substring)
print(results)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function **filter_by_substring** that takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. 

The code then defines a test case with a sample string and substring and prints the results, which should be the list of strings containing the substring.