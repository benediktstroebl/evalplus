Here is a Python script that contains a self-contained function that solves the problem of returning all prefixes from shortest to longest of an input string:
```python
from typing import List
import string

def all_prefixes(string: str) -> List[str]:
    return [''.join(w) for w in string.strip() if w != '']

# Test cases
test_cases = [
    'abc',
    'hello',
    '',
    'abc123',
]

for test_case in test_cases:
    print(all_prefixes(test_case))
```
This script defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest in a given string. It uses the general implementation to achieve this, and tests the function using the `test_cases` list.