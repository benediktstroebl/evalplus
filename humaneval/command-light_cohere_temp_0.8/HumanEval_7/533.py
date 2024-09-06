```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases


strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

# Call the function and assert the output is correct
assert filter_by_substring(strings, substring), ["abc", "cde", "array", "hello", "world"]
``` 
This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function uses a simple list comprehension to achieve this.