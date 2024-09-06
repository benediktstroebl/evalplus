```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings
    Returns:
    str: concatenated string
    """
    return "".join(strings)

# Test cases
test_cases = [
    [], ""
    ["a", "b", "c"], "abc"
    ["a", "bc"], "ab"
    [" ", "a"], "a"
]

for test_case in test_cases:
    actual = concatenate(test_case)
    expected = test_case[1:]
    assert actual == expected, f"test case {test_case} failed"
```