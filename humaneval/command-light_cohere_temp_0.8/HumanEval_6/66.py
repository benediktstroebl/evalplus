```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    out = []
    for char in s:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                out.append(0)
            stack.append(0)
        else:
                out.append(stack.pop()
               
        stack)
return out
```
This function takes a string as input and uses a stack to keep track of the nested parentheses. It iterates through string, and for each character, it decides whether to add the character to the stack (if it's '(')') or pop it off (if it's '(')'). It also keeps track of the deepest level of nesting, which helps to determine the correct level of each parenthesis.