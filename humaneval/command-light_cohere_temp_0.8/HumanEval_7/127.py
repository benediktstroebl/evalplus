```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases for the function
test_cases = [
    [],  # Empty list
    ['abc', 'bacd', 'cde', 'array'],  # Contains substring
    ['a', 'cup'],  # Does not contain substring
]

test_results = {}

for test_case in test_cases:
    actual = filter_by_substring(test_case, 'abc')
    expected = ['abc', 'bacd', 'cde', 'array']
    test_results[test_case] = actual == expected

print("Test results:", test_results)
``` 
This Python code defines a function `filter_by_substring` that filters a list of strings based on whether the given substring exists in each string. It uses the target a lists of test cases, each containing a list of strings and a substring, and then passes these test cases to the `filter_by_substring` function to verify its correctness. The function returns a results show whether the test cases passed were correctly filtered.