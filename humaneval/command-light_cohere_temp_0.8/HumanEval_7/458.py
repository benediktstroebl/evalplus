```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]

 # Sample test cases
test_cases = [
    [], 'a'
    ['abc', 'bacd', 'cde', 'array'], 'a'
    ['abc', 'a', 'bd'], 'a'
]

for test in test_cases:
    actual = filter_by_substring(test, 'a')
    assert actual == ['abc', 'a', 'bd'], "Actual: {}\nExpected: {}".format(actual, expected)
``` 
This script defines a function **`filter_by_substring`** that filters an input list of strings to retain only those that contain a given substring. The test cases are provided to demonstrate the functionality.

Note: You can expand this script by adding more test cases to cover different scenarios and edge cases of the filter function.