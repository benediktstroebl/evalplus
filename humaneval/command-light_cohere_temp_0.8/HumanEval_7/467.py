```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring."""
    return [string for string in strings if substring in string]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

results = filter_by_substring(strings, substring)
print(results)

strings = ["abc", "cde", "d"]
substring = "cd"

results = filter_by_substring(strings, substring)
print(results)
``` 
The function filter_by_substring takes a list of strings and a substring as input, and returns a new list of strings that contain the substring. The function uses the both input types as parameters and has comments to explain the code.

The function is then tested using two test cases, which pass without errors.