```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], '())':
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.append(level)
        result.append(stack.pop())
    return result
```

The algorithm uses the fact that the maximum depth of nesting is equal to the maximum length of a gap between opening and closing parentheses. It iterates through the string and keeps track of the current nesting level in a stack. When an opening parentheses is encountered, the nesting level is increased, and when a closing parentheses is encountered, the nesting level is decreased. The maximum nesting level is achieved when the parentheses are closing, and the length of the stack corresponds to the maximum depth of nesting. The reversed ('(()' zip '())') iteration is used to save the match iteration step.