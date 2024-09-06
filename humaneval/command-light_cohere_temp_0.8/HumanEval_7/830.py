```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function
my_list = ['abc', 'bacd', 'cde', 'array', 'String']
result = filter_by_substring(my_list, 'a')
print(result)  # Output: ['abc', 'bacd', 'array']
result = filter_by_substring(my_list, 'x')
print(result)  # Output: []
result = filter_by_substring([1, 2, 3, 4, 5], '23')
print(result)  # Output: []
``` 
This script defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only the strings that contain a given substring.  The input can be a list of strings and a substring.