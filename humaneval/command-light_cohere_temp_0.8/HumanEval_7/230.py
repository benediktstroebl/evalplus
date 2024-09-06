```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substrings = ['a', 'bd', 'cd', 'rad', 'world']
result = filter_by_substring(strings, substrings)
assert len(result) == 4  # Should be true
print(result)
``` 
This Python code defines a function `filter_by_substring` that filters a list of strings based on the presence of a given substring. The function utilizes a `List[str]`'s built-in function to iterate over the strings and checks if each string contains the provided substring using the `in` operator. The function returns a expected output: it filters the list of strings and returns a new list containing only the strings that contain the substring.