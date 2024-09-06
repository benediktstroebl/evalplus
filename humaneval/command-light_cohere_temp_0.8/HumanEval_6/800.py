Here's a self-contained Python script with a function `parse_nested_parens` that takes a string of nested parentheses as input and returns the deepest level of nesting for each group:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_parens = [')', '(', ')'
    closing_parens = [')', ')', ')'
    seen = set()  # Set to track seen characters
    for char in s:
        if char in opening_parens:
            stack.append(opening_parens.append(char))
            seen.add(char)
        if char in closing_parens:
            if not stack.pop():
                stack.append(closing_parens.pop()
           
   .stack.append(char)
       .
    # Recursively, and check for closing parenthesis until we reach the end of the string.
    is a way to return the stack, which contains the deepest level of nesting.
def parse_nested_parens(parentheses_string):
```