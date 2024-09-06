```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases:
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  
``` 
This script defines a function `filter_by_substring` that filters an input list of strings for a given substring. The test cases show that this function correctly outputs a list containing the strings that contain the given substring.