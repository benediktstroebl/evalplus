```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), nested_braces(s, '(')))))]

def nested_braces(s, brace) :
    stack = []
    for i, char in enumerate(s) :
        if char == brace: 
            stack.append(i)
        elif not stack or s[stack.pop()] == brace: 
            continue
        else:
            stack.pop()
    return stack
```