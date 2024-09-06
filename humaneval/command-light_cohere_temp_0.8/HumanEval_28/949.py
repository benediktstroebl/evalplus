```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return "".join("".join(strings))
all(char.join(c) == concatenate(['a' + c for c in strings]))
for i, s in enumerate(strings):
    assert s == concatenate([s + c for c in strings[i+1:]]), f"Incorrect concatenation at index {i+1}"
```