Here is a self-contained Python script that defines a function parse_nested_parens that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    sign = 1
    output = []
    for c in s:
        if c == '(':
            stack.append(sign)
        sign = -1
        elif c == ')':
            if len(stack) == 0:
                output.append(None)
            else:
                output.append(stack.pop())
                stack.append(sign)
            return output
```

The provided function, `parse_nested_parens`, takes a string `s` as input and uses a stack to keep track of open parentheses. It iterates over each input string character by character, starting with the current character. When it encounters an open parenthesis `(`),` it adds it to the stack, keeping the current `sign` as -1. When it encounters a particular close parenthesis `)`, it checks the length of the stack. If it's empty, it appends `None` to the `output` list. If there is not empty, it pops the top item from the stack, appends the `sign` to it, and then appends it to the `output` list. This effectively captures thetic logic of nesting multiple parentheses and returns the final list of parenthesis levels.