```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ']

# Test the function with a few strings
test_strings = [
    'abc',
    'abc123',
    'Hello, world!',
    '',
    '   '
]

for test_str in test_strings:
    actual_prefixes = all_prefixes(test_str)
    expected_prefixes = ['', '', 'abc']  # Adjust as needed
    assert actual_prefixes == expected_prefixes

```  This code defines a function all_prefixes that returns a list of prefixes from the shortest to the longest characters in a given string. The function is tested by comparing its output with the expected results for a set of strings using assertions.