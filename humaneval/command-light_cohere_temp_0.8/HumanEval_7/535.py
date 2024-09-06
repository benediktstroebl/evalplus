```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases 

strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a" 

print(filter_by_substring(strings, substring))  # ['abc', 'bacd', 'array'] 

strings = ["abracdc", "a", "hello", "hello"]
substring = "c" 

print(filter_by_substring(strings, substring))  # ['abracdc'] 

# Correct Outputs 

``` 
This script provides a self-contained function to filter an input list of strings for a given substring using the Python list comprehension.