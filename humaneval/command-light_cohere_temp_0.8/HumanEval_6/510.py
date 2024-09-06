```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            stack.append(stack.pop()
           
        fold = stack.append(c))
        if c == ')':
            stack.pop()
            if c == ')' and fold == 1:
                result.append(3)
            else:
                stack.append(fold)
                fold = stack.append(c)
    return result
```
This function, `parse_nested_parens`, takes a string of nested parentheses as input and returns a list of the deepest level of nesting of parentheses found. The function uses a list `stack` to keep track of the nesting levels and the current character. 

It iterates over each character in the string and adds the character to the stack if it is '(' or ')' (ignoring ')' for now). The function then adds the character to the stack if it is ')' and pops the character from the stack if it is '.'.

If the character is not ')' or is not the top-level parenthesis, then the function adds the current character to the stack. The function continues until all ')' characters have been added to the stack.

The function returns the list of the deepest level of nesting of parentheses found in the input string.