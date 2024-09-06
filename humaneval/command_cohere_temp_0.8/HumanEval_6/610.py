```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        for c in s:
            if c == opener:
                stack.append(stack[-1] + 1)
            elif c == closer:
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employed by the function `parse_nested_parens` is by tokenizing the input string `s` using the parentheses characters '(', ')' and then utilizing a stack to maintain the desired information. The stack is initialized with a sentinel value of 0, which represents the outermost parentheses. As the loop iterates through each character of the string, if a '(' is encountered, it is pushed onto the stack to track its nesting level. Conversely, when a ')' is encountered, it is popped from the stack, and the nesting level is subsequently decremented. The final nesting level of the parentheses is reflected in the last value of the stack, which is appended to the result list.