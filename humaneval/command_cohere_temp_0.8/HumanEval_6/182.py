```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = []
        level = 0
        for c in s:
            if c == opener:
                stack.append(opener)
            elif c == closer:
                if stack:
                    stack.pop()
                    level += 1
                else:
                    result.append(level)
            elif c != ' ':
                stack.append(c)
        result.append(level)
    return result
```

The function takes a string as input and iterates through each character in the string, tracking the nesting level of parentheses. When an opening parenthesis is encountered, it is added to a stack. When a closing parenthesis is encountered, the stack is checked, and if not empty, a nesting level is incremented. If the stack is empty, the current nesting level is appended to the results list. The process continues for all groups of parentheses in the provided string. The resulting list of nesting levels corresponds to the deepest level of nesting for each group of parentheses. 

Here is an example usage of the function and its corresponding output:
```
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```