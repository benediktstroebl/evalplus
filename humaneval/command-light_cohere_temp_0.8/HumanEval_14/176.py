```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string]

# Test cases
test_cases = [
    ("abc",),
    ("a",),
    (chr(97),),
    ("a", "bc"),
    ("ab", "ac"),
    ("", ""),
]

test_results = []
for text, expected in test_cases:
    actual_prefixes = all_prefixes(text)
    test_results.append(set(actual_prefixes == expected))

print("Test Results:")
for result in test_results:
    print(f" Got: {result}, Expected: {expected}")
```