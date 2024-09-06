```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = [0]
        closing_brackets = [0]
        level = 0
        for c in segment:
            if c == '(':
                level += 1
                open_brackets.append(level)
            elif c == ')':
                closing_brackets.append(level)
                level -= 1
        result.append(max(open_brackets))
    return result
```
The code processes each segment (separated by spaces) individually and keeps track of opening and closing brackets to determine the maximum nesting level. The maximum nesting level for each segment is then added to the result list.