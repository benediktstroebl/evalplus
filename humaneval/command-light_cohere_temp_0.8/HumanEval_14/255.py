```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix != '']

# Test cases
test_cases = [
    ("abc",),
    ("a",),
    ("a", "b", "a"),
    ("a", "b", "ab"),
    ("abac",),
    ("foo bar",),
    (""
]

test_results = []
for text, expected in test_cases:
    actual_prefixes = all_prefixes(text)
    test_results.append({'actual': actual_prefixes, 'expected': expected})

print("Test Results:")
for result in test_results:
    print(result)
```