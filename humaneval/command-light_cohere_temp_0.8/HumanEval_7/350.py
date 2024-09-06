Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "welcome", "good"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Test if the function works as expected
assert(result == ['abc', "bacd", "array"]), "Function does not return expected results"

print("Test passed")
```