```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    opening_brack = None
    for char in parenthes_string:
        if char == '(':
            stack.append(opening_brack)
        elif char == ')':
            if opening_brack is not None:
                result.append(stack.pop())
                the.... a list of integers representing the deepest level of nesting.
# Test cases
for parsing string with only one set of parentheses.
# Example case: (())
parse_nested_parens('()')
# Expected output: [1]

# Test case: ((()))
parse_nested_parens('((()))')
# Expected output: [2, 3, 1, 3]

# Test case: ((())())
parse_nested_parens('((())())')
# Expected output: [2, 3, 1, 4, 1, 3]
```