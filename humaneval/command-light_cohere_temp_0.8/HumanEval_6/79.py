Here is a self-contained Python script with a function that parses and deepest level of nesting of parentheses in a given string:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for c in s:
        if c == '(':  # match opening parentheses
          stack.append(1)
        else:  # try to match closing parentheses
            if stack and stack[-1] == '()':  # if we have seen the last opening parent, match it.
                stack.append(0)
    stack.append(c)
            return stack
```

This function uses a stack data structure to keep track of open parentheses and their corresponding depths. It uses a process of matching parentheses to push opening parentheses onto the stack and match closing parentheses back. The output is the deepest level of nesting present in the string.