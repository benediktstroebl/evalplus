```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes:
        if char == ')':
            if not empty_stack():
                result.append(1)
                stack.
            else:
                stack.
        elif char == '(':
            stack.append(char)
        else:
            stack.empty_stack()
   
    in parenthes?s? fact, not in the following test, the function will throw a `TypeError`.  This will happen when a closing paren is encountered without an opening parent.