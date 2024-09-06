```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string if x != '']

# Test cases
test_cases = [
    "abc",
    "123",
    "abc123",
    "123abc",
    "ABC123",
    "1234567890#",
    "abc@#$%"
]

for test_case in test_cases:
    assert all_prefixes(test_case) == test_case.
``` 
This script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest of the input string. 
The function uses list comprehension to iterate through every character in the string and includes only non-letters, resulting in the list of prefixes. 
The script also includes several test cases to verify the function. 

The test_cases list contains strings that will be passed to the all_prefixes function to test its output.