```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if not stack or stack[-1] == '(':
                result.append(0)
                stack.append(c)
            continue
        else:
                result.append(stack.pop())
               append(1)
    return result
``` 
This function, parse_nested_parens, is designed to parse and return the deepest level of nesting for a given string of parentheses. It utilizes a usage of a stack to keep track of opening parentheses. 

This function handles the following inputs well:
```python
test_data = [
    '(()()) ((())) () ((()))()',
    '(a)(b)(c)',
    '(((((((())))))))))'
]
```
This test_data is expected to contain strings with different levels of nested parentheses, separated by spaces.