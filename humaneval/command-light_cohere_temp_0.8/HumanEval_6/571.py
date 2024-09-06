```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack: List[int] = []
    output: List[int] = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            elif stack[-1] == '(':
                stack.append(len[output[-1]] + 1)
            else:
                stack.pop()
                stack[-1] = int(char)
    return output
# Example usage
parenthes_str = "(()()) ((())) () ((()))"
result = parse_nested_parens(parenthes_str)
print(result)
```