```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for match in parentheses_string.match(r'\([ ]*[^)]+\)'):
        content = match.group(0)
        if content:
            stack.append(content)
        else:
            while stack and stack[-1] != '(':
                stack.pop()
            stack.
            stack.push('(')
             if stack and stack[-1] == ')'.group():
                output.append(3)
                stack.pop()
                stack
                while stack.append(4)
    return output
```
This function iterates over each match found in parentheses_string. It uses the match() method from the re module to get a match object. The group() method is used to extract the match group. The content attribute of the match object is checked, and if it is not empty, it is pushed into the stack. Then, a nested loop is used to check if the stack contains an open parenthesis '(', and if it does, it is popped from the stack. If the stack is empty after this loop, then it is assumed that the current group in the stack is a closing parenthesis ')', and the next item in the stack is pushed into the output list as the third item.