```python
from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for parantices in parentheses_string.
    if not parantices is:
        stack.append(0)
    else:
        stack.append(1)  # Start with the first parenthesis
        stack.append(2)  # Start with the second parenthesis.
        stack.append(3)  # Start a new group
        stack.append(3)  # Continue with opening parenthesis until next closing parenthesis
        stack.append(4)  # Check if last closing parenthesis is matched
        result.append(stack.pop())  # Find the this group, we return the result list as a stack of nesting.
```