```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes_str:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                stack.pop()
                if stack[-1] == 1:
                    output.append(stack[-1])
            else:
                output.push(0)
    return output
``` 
This function takes a string of nested parentheses as input and returns a list of the deepest levels of nesting for each group of parentheses in the string. It does this by maintaining a stack of opening parentheses and appending the level to the output list when a closing parent is encountered. The function ensures that only the deepest level of nesting is returned by ignoring any further opening parentheses that are encountered.