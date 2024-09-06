```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    results = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                results.append(stack.pop()
               
            thes[ while stack and stack[-1] == ')' ][0] == 1
                stack.pop()
       ways.append(stack[3, 2, 1, 3])
                stack.append(1)
            else:
                stack.append(0)
    else:
        stack.append(int(match))
    return results
``` 
The function parse_nested_parens parses a string of nested parentheses and returns the deepest level of nesting. It uses a list stack to keep track of the nesting levels and pop the top element from the stack when it encounters a closing parent. The function also uses the list results to keep track of the matching groups.