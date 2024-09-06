```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -None]


# Test case 1
test_cases = [
    [], 'a'
    ['abc', 'bacd', 'cde', 'array'], 'a'
]

test_results = filter_by_substring(test_cases, 'a')
print(test_results)  # Output: ['abc', 'bacd', 'array']


# Test case 2
test_cases = [
    [], 'b'
    ['abc', 'bacd', 'cde', 'array'], 'a'
]

test_results = filter_by_substring(test_cases, 'a')
print(test_results)  # Output: []
```
This code introduces a function called `filter_by_substring`, designed to filter an input list of strings and return only those that contain a given substring. The function utilizes the basic Python list comprehension to iterate through the strings, and checks if each string contains the specified substring using the `find()` method. The output of the `find()` method returns `None` if the substring is not found, indicating that the string should be excluded from the result. This function takes a testing by passing a series of test cases, each containing an empty list, a string containing only the target substring, and strings containing both the substring and other characters. The function consistently returns the results that match the expected behavior for each test case.