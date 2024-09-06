```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(3)
            stack.append(c)
    else:
                stack.append(stack.pop())
   
        opening_level = stack.pop()
                closing_level = stack.pop()
                if closing_level == opening_level:
                    output.append(2)
                stack.append(c)
                else:
                    stack.append(stack.pop())
                   required any opening and closing, while a level of nesting.
def parse_nested_parens(input_string):
    return output
```