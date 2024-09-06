```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return "".join("".join(strings) if strings else "")
test_concatenate = [
    ["a", "b", "c"],
    [],
    ["foo", "bar"],
    ["abc"]
]
print(concatenate(test_concatenate))
```