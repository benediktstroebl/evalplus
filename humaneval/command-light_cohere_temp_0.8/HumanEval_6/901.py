```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening_paren_count = 0
    closing_paren_count = 0
    result = []

    for char in parentheses_string:
        if char == '(':
            opening_paren_count += 1
        stack.append(opening_paren_count)
        opening_paren_count = 0

    while stack:
        closing_paren_count += 1
        stack.append(closing_paren_count)
        closing_paren_count = 0

    while stack:
        result.append(stack.pop())

   
    all closing parentheses)

    return result
```
This code defines a function `parse_nested_parens` that accepts a string of nested parentheses and returns a list of the deepest level of nesting for each group of parentheses. The function uses a concept of a stack to keep track of opening and closing parentheses. It iterates through string character by character, and when it encounters an open parenthesis, it adds the count of open parentheses to the stack. Once all closing parentheses are read, the function goes through the stack and removes all the closing parentheses. This process continues until there stack is empty, at which point the deepest level of nesting for each group of parentheses is obtained.