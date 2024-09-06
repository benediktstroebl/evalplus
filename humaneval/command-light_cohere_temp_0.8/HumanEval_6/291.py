```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    for char in s:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] != 1:
                raise ValueError("Unmatched closing parenthesis.")
            stack.pop()
       
            if stack and stack[-1] == 1:
                raise ValueError("Nested parentheses not supported.")
    return stack

# Test the function
test_cases = [
    "(()()) ((())) () ((())()())",
    "()()()() ()",
    "((()))",
]

for tc in test_cases:
    actual = parse_nested_parens(tc)
    expected = [2, 3, 1, 3]
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"
```
The above code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting parentheses found. The function uses a `stack` to keep track of the nesting level of each open parenthesis. It iterates through to match the closing parenthesis to the appropriate open one. It also ensures that there are no nested parentheses by checking the stack at the same level.