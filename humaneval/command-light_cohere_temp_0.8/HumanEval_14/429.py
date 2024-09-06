```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(w for w in string if w.isalpha()) for i in range(len(string) + 1) if string[:i] != "" else "")
# Add test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("", []),
    ("123"), ["1", "12", "123"],
    ("abc123", ["abc", "123"]),
]

# Run function and compare results
for text, expected_result in test_cases:
    actual_result = all_prefixes(text)
    assert actual_result == expected_result, f"Mismatch for '{text}': Expected {'expected_result}', got {'actual_result"}
```