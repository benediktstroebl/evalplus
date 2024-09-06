```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function:
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Expected output ['abc', 'bacd', 'array']
``` 
This code defines a function called **filter_by_substring** that takes two parameters: a list of strings and a substring. The function filters this strings from the list and returns a new list that contains only the strings that contain the given substring.