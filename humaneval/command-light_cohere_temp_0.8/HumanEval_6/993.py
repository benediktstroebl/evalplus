```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for ch in s:
        if ch == '(': stack.append(0)
        elif ch == ')':
            stack.append(1)
            while stack.pop()
            return stack[
```
This function, `parse_nested_parens`, takes a string of nested parentheses as input and returns a list of their deepest nesting levels. The function uses a list comprehension to iterate over each character in the string. The function works by keeping a stack of opening parentheses and whenever a closing parenthesis is encountered, it appends 1 to the stack. Then, when an opening parenthesis is encountered, it pops the topmost element from the stack, which represents the deepest level of nesting for that group of parentheses.