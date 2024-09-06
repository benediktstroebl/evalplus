```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello world"]
substrings = ["a", "bc", "ade", "ar"]
test_strings = [f"filter_by_substring(strings, substring) for substring in substrings]
print(test_strings)  # Expected output: ['abc', 'bacd', 'array', 'hello world']
```  This code defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses a typing's `List` and `str` types and returns a list of strings that contain the substring. The test suite consists of creating a list of strings and substrings and passing them to the function. The test suite passes when the expected output of the function call is printed.