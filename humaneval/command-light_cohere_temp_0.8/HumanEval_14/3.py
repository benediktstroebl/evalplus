```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char != punctuation]

# Test cases
test_cases = [
    ("", ""),  # empty string
    "",         # empty input
    "abc", "abcd",  # single character
    "hello world",  # multiple characters
  ]

for case in test_cases:
    actual = all_prefixes(case)
    print(f"Input: {case}, Expected: {actual}")
``` 
This code defines a function `all_prefixes()` that returns a list of prefixes from the shortest to the longest of the input string. It filters out all character, non space characters and non-punctuation characters from the string.