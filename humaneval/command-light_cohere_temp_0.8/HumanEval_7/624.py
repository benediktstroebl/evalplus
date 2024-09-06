```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
test_strings = ['abc', 'bacd', 'cde', 'array', 'hello']
test_substrings = ['a', 'b', 'c', 'hello']

result = filter_by_substring(test_strings, test_substrings)

print(result)
``` 
The script defines a function **filter_by_substring** that filters a list of strings based on a given substring. It uses the particular list comprehension to iterate over the input strings and check if each substring is present in the string. The result is then returned as a new list containing only the strings that contain the given substring. 

The function is then tested by providing a list of strings and substrings and printing the resulting list.