```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    n = 0
    for c in s:
        if c == "(":
            stack.append(n)
            n += 1
        elif c == ")":
            if n == 0:
                raise ValueError("Unexpected close of a parenthesis.")
            stack.pop()
            if n == 3:
                return stack[:]
    return []

# Test cases
test_cases = [
    "(()()) ((())) () ((())())",
    "((((((())))))))",
    "((((()))()()())))"
]


for tc in test_cases:
    actual = parse_nested_parens(tc)
    assert actual == [2, 3, 1, 3]  # Example: [2, 3, 1, 3] is the deepest level of nesting.
```

Is there anything else I can assist you with?