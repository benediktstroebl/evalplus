```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Tests
strings = ['abc', 'bacd', 'cde', 'array', 'adfas']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
``` 
This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. It uses the the time typing with the List[str] parameter to specify that the input strings are strings, and the substring is also a string. The function uses a `in` operator to check if the substring exists in the strings. It returns a done list of strings that contain the substring.