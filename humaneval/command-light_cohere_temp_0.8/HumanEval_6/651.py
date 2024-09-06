```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string with nested parentheses as input and returns the deepest level of nesting as a list of integers.
    For example, the string '(()()) ((())) () ((()))' would return [2, 3, 1, 3].
    """
    result = []
    stack = []
    in_group = False
    for char in s:
        if char == "(" and not in_group:
            stack.append(1)
            in_group = True
        elif char == ")" and in_group:
            in_group = False
            if stack:
                result.append(stack.pop())
           
       
    stack.pop()
       
    stack
   result.append(1)
    return result
```