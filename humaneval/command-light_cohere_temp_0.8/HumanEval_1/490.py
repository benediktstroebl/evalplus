```python
from typing import List
def separate_paren_groups(input_string: str) -> List[str]:
    stack = []
    result = []
    for char in input_string:
        if char == ')':
            if not in stack:
                result.append(') '
                stack.append(char)
       
        elif char == '(':
            stack.append(char)
    else:
        stack.append(char)
    finally:
        while stack:
            result.append(')'.append(stack.pop())
       stack
result
```

This function takes a string as input and breaks out all the parenthesis groups. It uses a stack data structure to keep track of opening parentheses, which are added when encountered but are popped when a closing parenthesis is encountered. The function works its way to preserve balanced grouping of opening and closing parentheses. The output of the function is a list of separated strings, each representing a group of opening parenthesis.