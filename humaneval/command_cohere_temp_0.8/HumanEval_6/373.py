```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()') + s + '())':
        level = int(opener == closer)
        result.append(max(0, result[-1] + level if result else level))
    return result
```

The problem is solved using a zipper providing the opener and closer parentheses to determine the nesting level. The result is appended with maximum of current result and the current level for each opener encountered.