```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nested_parens in s.split():
        count = 0
        nested_level = 0
        stack = []
        for char in nested_parens:
            if char == '(':
                stack.append(char)
                count += 1
            else:
                count -= 1
                if count == 0 and stack:
                    nested_level += 1
                    stack.pop()
        result.append(nested_level)
    return result
```

The code uses a stack to track nested open parentheses '(' and decrements the count when it encounters a closing parenthesis ')' to determine the deepest level of nesting of parentheses in each group. It then provides an array of deepest levels for each group of parentheses.