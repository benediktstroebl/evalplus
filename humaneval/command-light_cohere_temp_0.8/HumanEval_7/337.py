```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]

# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'final']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
This Python code defines a function called `filter_by_substring` that filters a list of strings based on a given substring. The function takes two input arguments: `List[str]`, which represents the input list of strings, and `str`, which represents the substring to find in the strings.

It uses the `find()` method to search for the substring in each string and returns the strings that contain the substring, effectively filtering out all the strings that do not contain the substring.