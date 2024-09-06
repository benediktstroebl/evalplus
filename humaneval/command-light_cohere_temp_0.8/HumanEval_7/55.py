```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with example inputs and want results
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
This code defines a function **filter_by_substring** that filters a list of strings for a given substring. The function utilizes a list comprehension to iterate over each string and checks if the given substring exists in the string. 

This function is designed to be self-contained, and its purpose is to filter a list of strings based on a given substring.