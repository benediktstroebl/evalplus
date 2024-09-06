```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.strings if prefix != '' and len(prefix) > 0]

# Test cases
test_cases = [
    ("", []),
    ("a", ["a"]),
    ("abc", ["a", "ab", "abc"]),
    ("AcbC", ["a", "ab", "abc"]),
    # Long strings
    ("a", ["bc", "abc", "abcde"]),
    ("a", ["bc", "ab"]),
    # Different character
    "abc#def", ["ac", "ab"]
]

for text, expected_prefixes in test_cases:
    actual_prefixes = all_prefixes(text)
    print(f"Text: [{text}], Expected prefixes: [{', '.join(expected_prefixes)}])
    print(f"Actual prefixes: [{', '.join(actual_prefixes)}])
    assert actual_prefixes == expected_prefixes
```