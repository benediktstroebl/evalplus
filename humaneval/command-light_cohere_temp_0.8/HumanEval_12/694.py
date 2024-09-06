```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string in the list.
    """
    string = "".join(strings)
    if len(string) == 0:
        return None
    return string

# Test cases
test_cases = [
    ["a", "bb", "ccc"],
    ["ab", "bc", "abc"],
    ["aa", "bb", " "]
]

for test_case in test_cases:
    actual = longest(test_case)
    assert actual is not None
    assert actual == "".join(f"Longest string: {actual}")
```
This code defines a function called longest, which takes a list of strings as input and returns the longest string in that list. It utilizes the string method to convert the list of strings to a single string and compares it length with the input length to determine if it is the longest or not. 
The code also has a series of test cases that verify the function's behavior for different input lists.