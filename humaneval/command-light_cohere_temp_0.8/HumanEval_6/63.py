Here is a self-contained Python script that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening = 0
    closing = 0
    output = []
    for c in s:
        if c == '(':
            opening += 1
        else:
            closing += 1
        if opening == closing:
            stack.append(closing)
            opening, closing = 0
        else:
            if opening > closing:
                stack.append(opening)
                opening = closing + 1
            closing = 0
    return stack
# Test the function
test_str = '(()()) ((())) () ((())()())'
result = parse_nested_parens(test_str)
print(result)
```
This script defines a function `parse_nested_parens` that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. It uses a stack to keep track of opening and closing parentheses and iterates over the characters of the string.

The test string provided contains nested parentheses and the function should return the correct levels of nesting.