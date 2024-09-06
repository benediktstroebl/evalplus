```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':
            stack.append(0)
        elif c == ')':
            if stack:
                output.append(stack.pop()
               pop a partial match on the parenthesis in the stack, reset the stack.

# Example usage
s = "((()()) ((())) () ((())()()))"
print(parse_nested_parens(s))  # Output: [2, 3, 1, 3]
```
This code implements a function called `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. It uses a process that uses a stack to keep track of open parentheses, and when it encounters a '(', it appends a 0 to the stack. When it encounters a the open parenthesis, it checks the stack. If there are parenthesis in the stack, it adds the current character to the output list and populates the stack again.