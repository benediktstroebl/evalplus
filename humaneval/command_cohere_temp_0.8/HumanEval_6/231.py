```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('([{', ')]}'):
        stack = []
        level = 0
        for c in s:
            if c == opener:
                stack.append(opener)
            if c == closer:
                if stack:
                    level += 1
                    stack.pop()
                else:
                    result.append(level)
        if stack:
            result.append(level + len(stack))
    return result
```

The approach employs a straightforward recursive function with an activation record. Alternatively, you can use a stack to track the nesting level and iteratively process the string. This will eliminate the need for recursion and provide the same outcome.