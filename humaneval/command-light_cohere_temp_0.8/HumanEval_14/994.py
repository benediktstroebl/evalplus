```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '' and c not in [' ', '\n']]

# Test the function with some strings
test_strings = [
    "Hello World",
    "   Hello World   ",
    "Hello World!",
    "   HellO World   !",
    "abc",
    "ABC"
]

test_results = []
for text in test_strings:
    test_results.append(all_prefixes(text))

print(test_results)
```