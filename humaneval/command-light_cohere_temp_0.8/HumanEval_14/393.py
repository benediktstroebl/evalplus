```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '' and c not None]

# Test the function with various cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("", []),
    (".", ", [""])
]

for text, expected in test_cases:
    actual = all_prefixes(text)
    assert actual == expected, f"Error in test case: {text}"
```
The above code defines a function called all_prefixes, which returns a list of all prefixes of a given string. The function uses a simple Python list comprehension to filter out all non-empty characters from the input string and then includes them in the output list. The test_cases variable contains a few test cases, and the code iterates through each case to call the all_prefixes function and compare the actual output with the expected output.