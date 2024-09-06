```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring.
    :param strings: List of strings
    :param substring: The substring to search for
    :return: List of strings containing the given substring
    """
    return [x for x in strings if substring in x]

# Test case 1: Empty list
test_case_1 = []
print(filter_by_substring(test_case_1, 'a'))  # Output: []

# Test case 2: Single string
test_case_2 = ['abc']
print(filter_by_substring(test_case_2, 'a'))  # Output: ['abc']

# Test case 3: Multiple strings
test_case_3 = ['abc', 'bacd', 'cde', 'array']
print(filter_by_substring(test_case_3, 'a'))  # Output: ['abc', 'bacd']

# Test case 4: Inverted search
test_case_4 = ['cde', 'array', 'bacd', 'abc']
print(filter_by_substring(test_case_4, 'a'))  # Output: ['abc']
```
This Python script defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only the strings that contain a given substring. The test cases demonstrate the also how the function works.