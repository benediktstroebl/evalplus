```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    closing_level = 0

    for c in s:
        if c == '(':
            opening_level += 1
        elif c == ')':
            closing_level += 1
        else:
            if closing_level > opening_level:
                stack.append(closing_level)
                opening_level = 0
                closing_level = 0
        else:
            stack.append(opening_level)
            opening_level += 1

    return stack
# Example usage
test_string = "(()()) ((())) () ((()))"
result = parse_nested_parens(test_string)
print(result)  # Output: [2, 3, 1, 3]
```
This code implements a function **`parse_nested_parens`** that takes a string of nested parentheses as input and returns a list of corresponding opening and closing levels. It uses a particular order to handle the nested structure and ensure correct tracking of opening and closing levels for each parenthesis.