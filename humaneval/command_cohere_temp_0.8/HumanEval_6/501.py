```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair in s.split():
        level = 0
        i = 0
        while i < len(bracket_pair):
            if bracket_pair[i] == '(':
                level += 1
            else:
                level -= 1
            i += 1
        result.append(level)
    return result
```

This Python script includes a `parse_nested_parens` function, which takes a string as input and returns a list of the deepest levels of nesting for each group of parentheses. The string is split into list elements based on spaces, and for each element, the function maintains a `level` counter that keeps track of the depth of nested parentheses. The function increments the `level` for each opening paren and decrements it for each closing paren, providing the deepest level of nesting for each group.