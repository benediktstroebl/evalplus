Here is a self-contained Python script that solves the problem you described:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    stack = []
    for char in s:
        if char == '(': stack.append(1)
        elif char == ')':
            if stack: result.append(stack.pop()
                    done. Otherwise, stack.q.
            stack = []
       0
    done.stack.append(1)

return result
```
This function, parse_nested_parens, takes a string as input and returns a list of integer levels of nesting parentheses. It uses a stack data structure to keep track of open parentheses. 

The function iterates through each character in the string. It checks if the character is ')' or '(', it appends the corresponding number to the stack. If the character is neither ')' or '(', it moves to the next character in the string.