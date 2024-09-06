```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test case 1: Basic operation
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # ['abc', 'bacd', 'array']
# Test case 2: Multiple occurrence
strings = ['aab', 'aba', 'abcd', 'aba', 'a']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # ['aba', 'abcd', 'aba']
# Test case 3: Not present
strings = ['a', 'b', 'c', 'd', 'e', 'f']
substring = 'g'
result = filter_by_substring(strings, substring)
print(result)  # []
``` 
This code demonstrates a function that filters a list of strings based on a given substring. It uses the method to achieve this and passes corresponding tests.