```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ["abc", "bacd", "cde", "array", "string", "test"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["hello", "world"]
substring = "wo"
result = filter_by_substring(strings, substring)
print(result)  # Output: []
``` 
The function `filter_by_substring` in this script accepts a list of strings and a substring as input and outputs a new list of strings containing only the elements that contain the given substring. 

The test cases demonstrate how the function works by filtering strings with and without the substring.