```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bca", "cdef", "array", "hello", "world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bca', 'cdef', 'array']
```  This Python code defines a function called `filter_by_substring` that filters a list of strings based on whether the given substring appears in any of the strings. The function uses the expected typing (List[str]) for the strings and substring parameters, and returns a new list containing only the strings that contain the given substring. 

The code then creates a test list `strings` with several strings and a target substring, then calls the `filter_by_substring` function with those strings and substring, and stores the result in the `result` variable. The output will be the this list of strings that contain the target substring, which is ['abc', 'bca', 'cdef', 'array'] in this case.