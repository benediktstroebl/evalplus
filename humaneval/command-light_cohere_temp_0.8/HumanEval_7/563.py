```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Testing the function
test_strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
test_substring = 'abc'
result = filter_by_substring(test_strings, test_substring)
assert result == ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters a list of strings for a given substring. It uses the list comprehension to iterate over the input strings and checks if each string contains the given substring. The test section ensures that the function is working correctly by providing inputs and expected outputs for the function.