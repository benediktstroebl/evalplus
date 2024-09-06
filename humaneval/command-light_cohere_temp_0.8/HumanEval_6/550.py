Here is a self-contained Python script that solves the problem you described:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opened = False
    levels = 0
    result = []
    for c in s:
        if opened and c == "()":
            stack.append(levels)
            opened = False
        elif opened and c == "[]":
            stack.append(levels+opened = True)
        elif opened:
            if c == ")":
                stack.pop()
                opened = False
        elif c == "[":
                opened = False
            else:
                stack.append(levels)
        levels += 1
        result.append(stack.pop()
    more levels
        to follow the next []) pattern.
```

This script defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses in the string. It uses a open and closed parentheses to keep track of the nesting level and adds 1 to the current level for each open parent. The function uses a stack to keep track of the current level of opening parentheses and the deepest level of nesting is returned as the result.