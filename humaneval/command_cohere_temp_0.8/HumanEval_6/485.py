```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_parentheses = segment.count('(')
        close_parentheses = segment.count(')')
        result.append(max(open_parentheses, close_parentheses) - min(open_parentheses, close_parentheses))
    return result
```