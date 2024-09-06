Here's a Python script that contains a function called `separate_paren_groups` that solves the problem as described in the code block provided:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if stack:
                current_group = stack.pop()
            else:
                current_group.append(char)
        else:
            current_group.append(char)

    if stack:
        result.extend(stack)

    return result

# Add precomputed example tests
tests = [
    ("()", ['()']),
    ("(())", ['(())']),
    ("(()())", ['(()())']),
    ("( ) (( )) (( )( ))", ['()', '(())', '(()())']),
]

for inp, exp in tests:
    print(f"Input: {inp}")
    print(f"Expected: {exp}")
    print(f"Actual:  {separate_paren_groups(inp)}")
    print("---")
```

This script uses a stack to keep track of nested parentheses groups. It iterates through the characters of the input string, pushing a new group onto the stack whenever it encounters an open parentheses `(` and popping the stack whenever it encounters a closing parentheses `)`. Any characters that are not parentheses are added to the current group.

The script includes example tests where the input, expected, and actual results are printed for each test case. The expected results are provided in the code snippet you provided.