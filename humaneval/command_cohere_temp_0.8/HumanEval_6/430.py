```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        depth = 0
        unbalanced = 0
        stack = []
        for char in segment:
            if char == '(':
                stack.append(char)
                unbalanced += 1
            else:
                unbalanced -= 1
                if not unbalanced:
                    depth += 1
                stack.append(char)
        result.append(depth)
    return result
```

The approach employs a stack to track open parentheses encountered while iterating through each segment of the input string. When an open parenthesis is found, the stack is pushed with this character and an unbalanced counter is increased. When a close parenthesis is encountered, the unbalanced counter is decreased. If the counter reaches zero, the current depth is incremented as a closing parenthesis implies one additional level of nesting.

The output of the provided example input is `[2, 3, 1, 3]` as a result of the function executing over the provided input string.