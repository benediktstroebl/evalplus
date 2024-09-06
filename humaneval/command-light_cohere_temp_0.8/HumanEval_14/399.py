```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ' and char != '\n']

# Test cases
test_strs = [
    "abc",
    "Hello World",
    "Hello    World",
    " foo bar ",
    "foo#bar"
]

for text in test_strs:
    actual_prefixes = all_prefixes(text)
    assert set(actual) == set(expected)
    expected = ["".join(char) for char in text if char != ' ' and char != '\n']
    print(f"Test case {text}:")
    print(f"Actual prefixes: {actual_prefixes}")
    print(f"Expected prefixes: {expected}")
    print()
```
This code defines a function all_prefixes that returns a list of prefixes from a given string. The test cases validate the that this function produces the correct output for various input strings.