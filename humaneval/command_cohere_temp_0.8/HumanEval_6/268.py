```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for container, open, closed in zip(__find_containers(s), __find_opens(s), __find_closes(s)):
        result.append(len(container) - (open + closed))
    return result

def __find_containers(s: str) -> List[str]:
    return [i for i in s.split()]

def __find_opens(s: str) -> List[int]:
    return [i for i, char in enumerate(s) if char == '(']

def __find_closes(s: str) -> List[int]:
    return [i for i, char in enumerate(s) if char == ')' and i != len(s) - 1]
```