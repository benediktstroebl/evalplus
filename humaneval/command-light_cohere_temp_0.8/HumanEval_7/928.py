Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Testing the function
strings = ['abc', 'bacd', 'cde', 'array', 'dfff']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that filters an input list of strings and returns a new list that contains only the strings that contain a given substring. The function is then tested with a sample input and the output is displayed.