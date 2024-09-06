```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            else:
                stack.append(len[len(stack) - 1])
    return output
# Example usage
test_str = '(()()) ((())) () ((())()())'
test_output = parse_nested_parens(test_str)
assert test_output == [2, 3, 1, 3]
```