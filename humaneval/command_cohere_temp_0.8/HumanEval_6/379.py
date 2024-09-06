```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.append(level)
        result.append(stack.pop())
    return result
```

The approach employed by the function involves treating each group of parentheses as a nested stack, where incrementing and decrementing the `level` variable mimics opening and closing parentheses. The maximum value of the `level` variable during its execution corresponds to the deepest level of nesting for a particular group. The `zip('(()', '))'`)` method pairs each opening parenthesis with its corresponding closing parenthesis. Lastly, to ensure we get the deepest level of nesting for each set of parentheses, we discard the first element of the `stack` (which is always 0), and append the last element (which corresponds to the deepest level).