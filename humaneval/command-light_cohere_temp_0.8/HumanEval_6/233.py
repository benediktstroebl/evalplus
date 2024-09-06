```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    closing_level = 0
    parenthesis_count = 0
    for c in parenthes_string:
        if c == '(':
            opening_level += 1
        elif c == ')':
            closing_level += 1
        elif opening_level > closing_level:
            stack.append(opening_level)
        elif opening_level < closing_level:
            stack.append(closing_level)
        parenthesis_count += 1
    return stack
# Test the function with a string that passes the test
test_string = '(()()) ((())) () ((())()())'
result = parse_nested_parens(test_string)
assert len(result) == 5  # Ensuring the correct number of items in the stack
```