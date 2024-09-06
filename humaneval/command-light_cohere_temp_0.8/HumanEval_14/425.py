```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join([ch for ch in string if ch not in 'aeiou']) for _ in range(26)]
for x in range(26):
    assert all_prefixes("".join() == x, f"Failed test case {x}")
assert all_prefixes("abc") == ['a', 'ab', 'abc']
print("All prefixes passed the tests!")
```