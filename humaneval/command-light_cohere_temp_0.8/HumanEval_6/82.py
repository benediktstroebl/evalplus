Here's the code:

```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for match in parent_string.group(r'\(\)[ !]+'):
        stack.append(1)
        if match == '(':
            stack.append(0)
        while match == ')':
            if len(stack) > 0 and stack[-1] == 1:
                stack.pop()
                if len(stack) == 0:
                    result.append(0)
            stack.append(1)
   if match == '(':
                stack.append(1)
            while match == ')':
                    if len(stack) > 1:
                        stack.pop()
                    result.append(stack[-1])
    return result
```

This function uses a stack to keep track of open parentheses. It iterates through the string and adds the current character to the stack if it is '(' or ')', and removes it from the stack if it is ')' or is empty. The function returns the deepest level of nesting found in the string. 

Note: The code assumes that the input string follows the format of a group of parentheses.