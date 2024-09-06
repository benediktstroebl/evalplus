```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = [0]
        for ch in s:
            if ch == opener:
                stack.append(stack[-1] + 1)
            elif ch == closer:
                stack.pop()
            else:
                pass
        result.append(stack[0])
    return result
```

The approach uses a generator expression and the zip function to iterate through the opener and closer pairs of parentheses, incrementing the stack for each opener and decrementing for each closer. The maximum value in the stack is the deepest level of nesting for each group. The overall time complexity of the program is O(n), where n is the number of characters in the string. 

To understand this solution more comprehensively, try debugging it step by step, and if any doubts still remain, kindly ask for further clarification.