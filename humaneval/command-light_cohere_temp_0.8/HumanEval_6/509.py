```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[str] = []
    result: List[int] = []
    for t in s:
        if t == '(':
            stack.append(')')
        if stack[-1] == '(':
                stack.append(')')
            else:
                stack.append(t)
        else:
                stack.append(t)
    if t == ')':
                    result.append(stack.pop())
                    stack.pop())
                    stack.append(')')
    important list(result)
    return result
# Examples:
test_cases = [
    "(()()) ((())) () ((())())",
    "((()))",
    "((()))()()",
    "())()()()",
    # "(((((()))))))"
]

for case in test_cases:
    assert parse_nested_parens(case) == [2, 3, 1, 3]
```