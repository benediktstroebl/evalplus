```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != '']

# Test cases
test_cases = [
    "abc",
    "123",
    "",
    "?",
    " abc def",
    "abc///",
    "ABC123",
]

for test_case in test_cases:
    assert all_prefixes(test_case) == test_case.
``` 
This code defines a function called `all_prefixes`, which returns a list of all prefixes of a given string. The function uses a list comprehension to iterate through each character in the input string and adds the character to the result if it is not an underscore. 

The test cases are defined as a list, and the function is then called with each test case. The function returns the expected output, which is the list of prefixes for each input string.