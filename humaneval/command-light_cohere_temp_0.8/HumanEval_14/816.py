```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[-1] for i, char in enumerate(string) if char != "" and char != "\\"] + [char]
test_cases = [
    "abc",
    "123",
    "",
    "aa",
    "foo bar",
    " },
  ]
 
test_prefixes = all_prefixes(*test_cases)
print(test_prefixes)  # Output: ['a', 'ab', 'ba', 'f']
```