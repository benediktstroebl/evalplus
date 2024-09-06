```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.a if prefix != '']

# Test cases
test_cases = [
    ('ab', ['ab']),
    ('', ['a']),
    ('abc', ['a', 'ab', 'abc']),
    ('', []),
    ('a', ['a']),
    ('a', ['ab', 'abc'])
]

for case, expected in test_cases:
    actual = all_prefixes(case)
    assert actual == expected, f"Error in test case [{case}] - Expected {expected}, got {actual}"
```  This script defines a function all_prefixes that returns a list of all prefixes in a given string. It uses list comprehension and a generator expression to iterate through each character in the string, and includes only the prefixes that are not spaces in the resulting string. The test cases ensure the