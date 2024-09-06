```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.contains(substring)]


 # Test cases
strings = ['abc', 'bacd', 'cde', 'array', 'hello', 'world']
substrings = ['a', 'bcd']

print(filter_by_substring(strings, substrings))  # Output: ['abc', 'bacd']
``` 
This Python code defines a function `filter_by_substring` that filters a list of strings based on whether the strings contain a given substring. It uses the generation testing to create a list of strings and a list of substrings. The `filter_by_substring` function then returns a new list containing only the strings from the original list that contain the given substring.