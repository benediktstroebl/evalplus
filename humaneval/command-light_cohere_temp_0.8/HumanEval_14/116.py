```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']

# Test cases for all_prefixes function
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("a", ["a"]),
    ("", []),
    ("123", ["1"]),
    ("abc123", ["a", "bc", "123"]),
]

for case in test_cases:
    actual = all_prefixes(case)
    assert actual == case, f"Failed for case: {case}"
``` 
This Python script defines a function all_prefixes that returns a list of all prefixes from the shortest to longest in a given string. It utilizes list comprehension with a condition to filter out any characters that are not letters, which are removed from the string. The function then has test cases that cover a variety of scenarios, such as passing an empty string, a string with only one character, a string with only digits, and a string with various characters and lengths.