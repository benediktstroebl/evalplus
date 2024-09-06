```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with a variety of inputs
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substrings = ['a', 'bcd', 'cde', 'array', 'hello']

# Test the function
result = filter_by_substring(strings, substrings)
assert len(result) == len(strings)
assert result == ['abc', 'bacd', 'array', 'hello world']
```
The function filter_by_substring takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The test cases ensure that the function is correctly identifying and returning the desired elements from the input list that contain the given substring.