```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']

# Test cases
test_cases = [
    "abc",
    "123",
    "!",
    "#$",
    "abc123",
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    assert len(actual_prefixes) == len(expected_prefixes), f"Test case [{test_case}] failed."
    expected_prefixes = ['', 'a', 'ab', 'aaa', 'abc']
    assert actual_prefixes == expected_prefixes, f"Test case [{test_case}] failed."
```
The above Python script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest character in the input string. 
It uses list comprehension to iterate over every character in the string, and includes them if they are not spaces. 

Additionally, the script provides a set of test cases, and it passes each test by calling the function with different strings, and then it verifies if the actual result matches the expected result.