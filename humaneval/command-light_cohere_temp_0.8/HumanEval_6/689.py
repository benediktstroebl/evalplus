```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    result: List[int] = []
    opening_levels = 0
    closing_levels = 0

    for level, char in enumerate(s, 1):
        if char == '(':
            opening_levels += 1
        elif char == ')':
            closing_levels += 1
        else:
            opening_levels -= 1
            closing_levels -= 1

        if opening_levels > closing_levels:
            stack.append(level)
        result.append(stack.pop(stack). Shaker(stack))
        stack.pop()

    stack
    repeated ( ) to make sure there's no unmatched opening parenthesis)
    return result
# Example usage
input_string = '(()()) ((())) () ((()))'
print(parse_nested_parens(input_string))
 ```