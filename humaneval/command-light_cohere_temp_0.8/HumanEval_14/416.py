```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.getprefixes(string) if prefix != "" and prefix.get(0) != "" and prefix[0] != " "]

# Test case:
test_string = "abc"
test_cases = [
    test_string,
    "",  # empty string
    "",  # empty single character
    "abc",  # character prefix
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    assert len(actual_prefixes) == 3
    assert actual_prefixes == [
        "", "abc", "ab"]
    ]
```  This code defines a function all_prefixes that returns a list of all prefixes of a given string. The function uses a Python built-in function getprefixes, which generates all prefixes of a given string.

The test case section contains a list of test cases, with different lengths and contents, and uses assertions to check if the function's output matches the expected output.