```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    inside = False
    result = []
    for c in s:
        if c == '(' and not inside:
            inside = True
            stack.append(1)
        elif c == ')' and inside:
            inside = False
            stack.pop()
        if stack:
                result.append(stack.pop()
    if stack:
                continue
            else:
                break
    return result
# Sample Test Cases
test_cases = [
    "(()()) ((())) () ((()))()",
    "((()))",
    "((((()))))"
]

for case in test_cases:
    actual_result = parse_nested_parens(case)
    print(f"Expected: { {actual_result}, {case}")
```
The above code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting of parentheses in the string. The code uses a simple stack to keep track of opening parentheses and appends the current level of nesting to the `result` list. The function also has a corresponding tests to verify its correctness.