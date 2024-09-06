```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        cnt = 0
        for j, c in enumerate(char):
            if c == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                result.append(cnt)
                break
        if cnt > 0:
            result.append(cnt)
    return result
```

The code processes each group of parentheses separately and keeps track of the nesting level with a counter. When the counter is positive, it indicates the current depth of nesting. The function sets the list `result` with the maximum depth of nesting in the `[]` and terminates the loop if it finds a closing parenthesis. The `enumerate` function is used to track the position of each character to measure the depth of nesting.