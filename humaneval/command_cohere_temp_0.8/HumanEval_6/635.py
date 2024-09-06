```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair_str in s.split():
        level = 0
        unbalanced = 0
        stack = []
        for char in bracket_pair_str:
            if char == '(':
                stack.append(char)
                unbalanced += 1
            else:
                unbalanced -= 1
                if not unbalanced:
                    level += 1
                    if stack:
                        result.append(level)
                        stack.pop()
                stack.append(char)
        if unbalanced > 0:
            result.append(level)
    return result
```

The reasoning behind the correct solution is Nested parentheses can be represented as a balanced binary tree. The maximum depth of a binary tree of n nodes is `Log2(n) + 1`. Therefore, the maximum depth of nesting can be calculated by adding one to the log2 of the number of parentheses groups. This is calculated using the count of unbalanced parentheses, which gives the number of nodes, and the loop in the bracket_pair_str iteration.