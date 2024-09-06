```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    result = []
    for p in parentheses:
        if not nested:
            nested = []
        elif not open:
            nested.append(p[::-1])
        else:
            nested.append(open)
            nested.append(p)
            nested.append(close)
        result.append(p[::-1])
    return result
```