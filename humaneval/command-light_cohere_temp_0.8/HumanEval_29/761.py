```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"

test_strings = [
    "This is text with prefix: abc",
    "Another, longer text with same prefix",
    "Everything is fine, but not with 'a'" prefix"
]

test_cases = {
    "text with specific prefix": [filter_by_prefix(strings, prefix)],
    "List with a prefix": [],
    "Strings with no prefix": ["apple", "orange"],
    "Long text with other prefix": test_strings[2:]
}

for name, test_case in test_cases.items():
    print(f"Test {}: ".format(name))
    assert filter_by_prefix(strings, prefix) == test_case, "Error in test: {}"

print("All tests passed!")
```