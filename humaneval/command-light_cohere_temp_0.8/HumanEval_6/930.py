```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i+1)
        elif char == ")":
            if len(stack) == 0:
                output.append(i)
            stack.clear()
       
        out_list = [i+1] + stack
            output.append(len(out_list))
            stack = []
        else:
            stack.append(i)
    return output
```
This code implements a function called `parse_nested_parens` that parses and returns the deepest level of nesting for a string of parentheses. The function uses a `enumerize` function to iterate over the characters in the string. It uses a `stack` list to keep track of the stack of open parentheses and appends the current character to the stack. The function then checks the character `)()` to close the stack and appends the current index to the `output` list. The `stack` list is then cleared to start a new stack for the next character. Finally, the function returns the `output` list, which contains the deepest level of nesting for each group of parentheses in the string.