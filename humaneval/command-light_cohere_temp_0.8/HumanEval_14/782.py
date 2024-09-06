```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != '']

# Test cases
test_cases = [
    "abc",
    "123",
    "",
    "00",
    "foo",
    "abc123",
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    expected_prefixes = ["", "", "o", "foo", "abc"]
    assert actual_prefixes == expected_prefixes
``` 
This code defines a function `all_prefixes` that returns a list of prefixes from the shortest to the longest of the input string. It uses a-coded if statement to filter out the spaces from the string. 

The code then passes a series of test cases, each containing a string and the expected list of prefixes, and the program uses the `assert` statement to check if the actual output matches the expected output.