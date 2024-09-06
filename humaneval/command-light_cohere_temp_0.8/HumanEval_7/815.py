Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for those that contain a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 a

	# tests
test_strings = ['abc', 'bacd', 'cde', 'array', 'quick', 'test']
test_substring = 'a'
test_result = filter_by_substring(test_strings, test_substring)
print(test_result)  # Output ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as arguments and returns a new list of strings that contain the substring. The tests are a strings and substring.  that are passed to the function and the expected output is printed.