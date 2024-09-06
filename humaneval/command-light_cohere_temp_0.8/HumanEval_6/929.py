Here is a self-contained Python script with a function that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(': stack.push(1)
        if c == ')':  stack.pop()
       separ(stack)
        else: stack.append(int(c))
        result.append(stack)
    return result
    # Example usage:
    s = '(()()) ((())) () ((())()())'
    return parse_nested_parens(s)
```
This function takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses. It works by maintaining a stack of open parentheses and their corresponding depths. The function iterates through each character in the string. Each time it encounters an open parenthesis ('), it pushes the depth of nesting one onto the stack. Then, when it encounters a close parenthesis, it pops the depth of nesting from the stack, and appends it to the result. The function continues iterating through each character in the string until all parentheses are processed.