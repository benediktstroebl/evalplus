Here is a self-contained Python script that solves the problem of parsing and identifying the deepest level of nesting in a given string of parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] == 1:
                stack.pop()
           else
               else:
                stack[-1] += 1
    return stack
# Test the function
test_string = "(()()) ((())) () ((()))"
result = parse_nested_parens(test_string)
print(result)
```
The function parse_nested_parens takes a string as input and uses a stack to keep track of opening parentheses. It iterates through string character to determine if the current character is an open parenthesis '(', in which case it is pushed onto the stack, or if it is a close parenthesis ')', the function checks if the stack is empty or the top item is 1, which means we have reached the deepest level of nesting, and the function pops the last item from the stack. Then, if the stack is not empty and the top item is not 1, the item is incremented by 1, effectively going one level deeper into the nesting.