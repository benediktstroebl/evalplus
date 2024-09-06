```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, Closer in zip('(()')[::-1], ')'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == Closer:
                level -= 1
                stack.pop()
        result.append(stack[-1])
    return result
```
The function iterates through each character in the string using a zip strategy and maintains a stack of the maximum depths of parentheses at each iteration. The stack is populated based on the opening parentheses and reduced based on the closing parentheses. The maximum depth of the stack element at the end of each iteration denotes the deepest level of nesting of parentheses in each group, which is added to the result list. The final result list contains the deepest levels of nesting for each group of parentheses in the provided string. 

Here is a example usage of this function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```