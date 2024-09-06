```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -None]


# Testing the function
test_strings = [
    "This is a test string",
    "This has an elemental text",
    "Search string, but also"
]

test_substring = "elemental"

result = filter_by_substring(test_strings, test_substring)

print("Results:", result)
```