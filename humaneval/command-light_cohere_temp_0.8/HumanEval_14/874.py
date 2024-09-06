```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.md
        """ "abcdefghijklmnopqr"[::-1]]

# Test cases
test_cases = [
    "abcdefghijklmnopqr",
    "aa",
    # Add more test cases here
]

for test_case in test_cases:
    print(all_prefixes(test_case))
```
The function all_prefixes takes a string as input and returns a list of its prefixes from shortest to longest. The function uses a set comprehension to iterate over the characters in the string and adds each prefix to the result.