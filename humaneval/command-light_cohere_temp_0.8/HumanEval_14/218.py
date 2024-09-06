```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[i:i+2] for i in range(len(string)) if string[i:i+2].isalpha() and string[:i] == string[i:]]

# Test case: Check all valid prefixes of "abc"
test_cases = [
    ("", ["a", ""])
    ("ab", ["ab", ""])
    ("abc", ["abc"])
    # Add more test cases here
]

for prefix, expected_prefixes in test_cases:
    actual_prefixes = all_prefixes(prefix)
    assert all(actual_prefixes == expected_prefixes)
```  This code defines a function `all_prefixes()` that returns a list of all prefixes from shortest to longest of the input string. The function uses a slicing technique to extract all prefixes. It uses the testing cases to verify the functionality of the `all_prefixes()` function with different input strings.