```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        level = 0
        stack = []
        for c in segment:
            if c == '(':
                stack.append(c)
            else:
                if not stack or stack.pop() != '(':
                    continue
                level += 1
        result.append(level)
    return result
```

The nested parentheses in the input string `s` are split into segments and a list of maximum depths (levels of nesting) is kept for each segment. The depth is increased whenever an opening parenthesis `(` is encountered, but it is decreased only when a closing parenthesis `)` is encountered and the last item in the stack is an opening parenthesis.