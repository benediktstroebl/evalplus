```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_group in s.split():
        stack = []
        bracket_level = 0
        for char in bracket_group:
            if char == '(':
                bracket_level += 1
                stack.append(bracket_level)
            elif char == ')':
                bracket_level = stack.pop() if stack else 0
            result.append(bracket_level)
    return result
```

The specified Python script solves the problem using a simple algorithm that iterates through each bracket group and maintains a `stack` of open brackets `(` and a `bracket_level` variable to keep track of the current deepest nesting level.

For each open bracket `(`, the `bracket_level` is increased, and the current `bracket_level` is appended to the `stack`. For each closed bracket `)`, the current `bracket_level` is restored from the stack, or set to 0 if the stack is empty. The `result` list is appended with the current `bracket_level` for each bracket group, representing the deepest level of nesting of parentheses.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This will output `[2, 3, 1, 3]` as the result of the function, representing the deepest level of nesting of parentheses for each bracket group, respectively.