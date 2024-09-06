```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != '']

# Test cases for function:
test_cases = [
    'abc',
    '',
    '123',
    'abc123',
    'aa',
    'a123'
]

for test_str in test_cases:
    actual_prefixes = all_prefixes(test_str)
    assert len(actual_prefixes) == len(set(actual_prefixes)), \
        f"Error: {test_str} should have {actual_prefixes} as prefix list, but doesn't."
``` 
This code defines a Python function all_prefixes that returns a list of prefixes from a given string. It uses a specific input, a string, and passes it to the function.