Here is a self-contained Python script that defines a function parse_nested_parens that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    output: List[int] = []

    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            else:
                stack.append(stack.pop())
               while c == ')', pop it from stack, and append the top element of the stack to output.

def test_parse_nested_parens():
    s = "((()()) ((())) () ((())())"
    assert parse_nested_parens(s) == [2, 3, 1, 3]
```
The `parse_nested_parens` function uses a stack to keep track of the nesting level. It iterates over each input string, and for each character, it decides whether to add it to the stack or push it to the output list based on whether it is a '(' or ')' character.