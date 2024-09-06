```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(i) for i in string if i != ""]

# Test the function with a few cases
test_cases = [
    "abc",
    "123",
    "hello world",
    " ",
    "ABCDEFGHIJKLMNOPQRSTUVWSXYZ"[::-1] # Use a character not in the alphabet
]

test_results = []
for case in test_cases:
    test_results.append(all_prefixes(case))

print("Test Results:", test_results)
```