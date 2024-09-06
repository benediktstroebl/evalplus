Here's the corrected version of the Python script with self-contained code:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    start_level = 0
    for c in s:
        if c == '(':
            start_level += 1
        elif c == ')':
            start_level -= 1
        stack.append(start_level)
    return stack
```

This script defines a function `parse_nested_parens` that takes a string `s` as input and returns a list of integers `[start_level, ...]`. The function uses a stack to keep track of the nesting level of each opening parenthesis. The function iterates over each character in the string, checking if it's an opening parenthesis `( )` and, if so, increments the nesting level. If it's is a closing parenthesis `)`, it decrements the nesting level and pushes the current level to the stack. If the character isn't a parenthesis, the function adds the current nesting level to the stack.

This function effectively parses and reassembles the nested parentheses in the input string, returning the deepest level of nesting of parentheses.