```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join("".join([string[i:]+() for i, s in enumerate(string) if s!isalpha())))
# Test cases
test_cases = [
    "", ""
  , "   "
  , "abc"
  , "abc123"
  , "Asdfg Scotch!"
]

for test_case in test_cases:
    print(test_case)
    print(all_prefixes(test_case))
    print()
```
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of an input string. 

This is a common problem with many interesting variations, and the solution is self-contained within the function.