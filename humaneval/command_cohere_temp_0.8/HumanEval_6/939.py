```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = [0]
        level = 0
        for ch in s:
            if ch == opener:
                level += 1
                stack.append(level)
            elif ch == closer:
                level = stack.pop()
            elif not stack:
                result.append(level)
        if stack:
            result.append(stack.pop())
    return result
```

The provided Python script defines a function called `parse_nested_parens` that takes a string as input and returns a list of deepest levels of nesting of parentheses in each group separated by spaces.

The function uses a list `stack` to keep track of the current depth of parentheses nesting. It iterates through the characters of the input string, increasing the `level` counter when it encounters an opening parenthesis and decreasing it when it encounters a closing parenthesis. When the closing parenthesis doesn't have a matching opening one, the `stack` ensures it still gets properly balanced and the last value is added. The result is a list of these `level` values, which represents the deepest level of nesting for each group of parentheses.