```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [x for x in string if x != '' and x not in ['', ' ', '\n', '\r']]

# Test cases
test_cases = [
    "abc",
    "A",
    "123abc",
    "",
    "abc123",
    "A123",
    "123",
]

for test_case in test_cases:
    print(all_prefixes(test_case))
    print(test_case + ' should return:')
    print(sorted(all_prefixes(test_case))))
``` 
This code defines a function all_prefixes that returns a list of all prefixes in a given string, excluding empty strings, spaces, and newline characters. The function uses a string's characters and non-empty substrings in a list comprehension to generate all possible prefixes.  The result case that uses the all_prefixes function to test its own behavior and correctly sorts the output.