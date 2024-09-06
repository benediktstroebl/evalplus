```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with a sample input and expected output
strings = ['abc', 'bacd', 'cde', 'array', ' welcome', '!are']
substring = 'a'

# Test case 1: Should return ['abc', 'bacd']
test_case1 = filter_by_substring(strings, substring)
assert test_case1 == ['abc', 'bacd']

# Test case 2: Should return []
test_case2 = filter_by_substring(strings, substring)
assert test_case2 == []

# Test case 3: Should return ['array']
test_case3 = filter_case3 = filter_by_substring(strings, substring)
assert test_case3 == ['array']
```
This Python script defines a function `filter_by_substring` that takes two parameters: a list of strings and a substring. The function filters this strings from the list and returns a new list containing only the strings that contain the given substring. It is also has a set of test cases that validate the correctness of the `filter_by_substring` function.