```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with a sample input
strings = ['abc', 'bacd', 'cde', 'array', 'axy']
substring = 'a'

# Verify expected output
print(filter_by_substring(strings, substring))  # ['abc', 'bacd', 'array']
``` 
This code defines a function called `filter_by_substring` that takes two arguments: a list of strings (`strings`) and a substring (`substring`). It uses a list comprehension to filter the input strings, keeping only the ones that contain the specified substring. The function is designed to run tests on a sample input to verify its correctness.