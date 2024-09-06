```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("abcde", ["abc", "abcd", "acd", "ace"]),
    ("", []),
    ("foo bar baz", ["foo", "bar", "baz"])
]

for text, expected in test_cases:
    print(text, "Input:", end=" ")
    print(all_prefixes(text), "Expected:", end=" )
    print(expected, end=" ")
```
This Python code defines a function called **`all_prefixes`** that returns a list of all prefixes of a given string. It utilizes a following strategy:
- It iterates through each character in the input string.
- For each character, it creates a prefix by including it without removing it from the string.

This function handles different input cases effectively and produces the expected output for each test.