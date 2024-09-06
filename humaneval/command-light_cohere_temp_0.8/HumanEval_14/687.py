```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in string if i != ""].strip() for i]

# Test cases
test_cases = [
    "",
    "abc",
    "123",
    "abc123",
    "1234567890",
    "abc1234567890",
]

for test_case in test_cases:
    print(test_case)
    actual_prefixes = all_prefixes(test_case)
    expected_prefixes = ["", "", "abc", "", "abc", "abc", "abc123"]
    print(f"Expected: {expected_prefixes}")
    print(f"Actual: {actual_prefixes}")
    print()
```
This Python code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of an input string. 

The function uses a generator expression with the start variable and the strip method to generate all prefixes, and then uses a list comprehension to filter out the empty characters. 

The code then tests the function with several input strings and compares the actual output with the expected output.