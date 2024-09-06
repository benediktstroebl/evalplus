```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in range(len(string))][:1] if string[i] != "" else "" for i in range(1, len(string))]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("hello world", ["h", "el", "llow", "world"]),
    ("", [""])
]

for case in test_cases:
    print(case, all_prefixes(case)))
```