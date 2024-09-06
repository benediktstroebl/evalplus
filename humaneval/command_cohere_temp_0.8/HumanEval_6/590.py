```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        level = 0
        stack = []
        for c in token:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The nested parentheses in the input string `s` are split into individual tokens and the deepest level of nesting for each token is computed in this function. It does this by maintaining a `level` counter that increments when `(` characters are encountered and decrements when `)` characters are encountered. The count is accumulated in the `result` list.