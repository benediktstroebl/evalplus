```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = []
        level = 0
        for ch in s:
            if ch == opener:
                stack.append(level)
                level += 1
            elif ch == closer:
                level -= 1
                stack.pop()
        result.append(level)
    return result
```

The approach employed by the function involves treating each group of parentheses as a nested stack, where incrementing and decrementing a `level` variable is done accordingly as openers and closers are encountered. This `level` variable represents the depth of the currently ongoing nesting. A list `stack` is used to keep track of the different grouping depths. Consequently, the final list of deepest nesting for each group is the output.