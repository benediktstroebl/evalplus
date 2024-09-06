```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Parse a string with nested parentheses and return the deepest level of nesting.
    Example: Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    Returns the array of the deepest level of nesting.
    """ Example:
      - [(),()(),  )
      => [2, 3]
    """
    stack: List[List[int]] = []
    in_parentheses: List[int] = []
    for char in s:
        if char == ')':
            stack.append(in_parentheses)
            in_parentheses.append(0)
        elif char == '(':
            in_parentheses.append(1)
            stack.append([in_parentheses])
        stack.pop()
        add 1
        stack.append([in_parentheses])
        in_parentheses.pop()
        add (2) to stack
        stack.append([in_parentheses])
        in_parentheses.pop() add (2) to stack
        return stack.
```

Test cases:
```python
# Test cases
test_cases = [
    ("(()())((()))()((()))()()()()",
    "(()())()()()(()())()()()()()()()",
    "((()))()()((())()())",
    "(()())()()(()())()()()()()()",
    # Add more test cases as needed
)

for s, expected in test_cases:
    actual = parse_nested_parens(s)
    assert actual == expected
```

This script defines the function parse_nested_parens which takes a string as input and returns the deepest level of nesting of parentheses. It uses a nested stack and list of in-parentheses to keep track of the open and closed parentheses. The stack is used to keep track of the last added element, and the in-parentheses list is used to keep track of the open parentheses.  The function iterates over the string and adds the appropriate elements to the stack and in-parentheses lists. It then returns the stack, which will contain the deepest level of nesting of parentheses.