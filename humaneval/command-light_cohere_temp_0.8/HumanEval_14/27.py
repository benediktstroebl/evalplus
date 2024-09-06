```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join("".join(c) for c in string if c.isalpha())]

# Test cases
tests = [
    ("abc", ["a", "ab", "abc"]),
    ("", [""])],
    ("def", []),
    ("this", ["is", "t", "h", "e", "t", "h"]),
    ("", []),
    ("\t\n", ["\t", "\n"])
]

for input_, expected in tests:
    print(input_, " -> ", end="")
    print(all_prefixes(input_)))
    print("-" * end=")
    print(expected)
```