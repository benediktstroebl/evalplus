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
                stack.pop()
        result.append(stack[-1])
    return result
```

The approach employs a counter `level` to keep track of the current nesting level, and a `stack` to keep track of _maximum depth of nesting_ for each group. Whenever an opening parenthesis is encountered, its nesting level is recorded and the `level` is incremented. On encountering a closing parenthesis, the `level` is decremented and when it falls to zero, the last value of the `level` is popped from the `stack`, providing the maximum depth of nesting for the just concluded group. The process is reversed using list comprehension to parse backwards through the string and the result is a list of maximum depths for each group of parentheses. 

This code uses Python's typing module to infer types, but the code should still work without type declarations.