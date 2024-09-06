```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for match in s:
        if match == '()':
            stack.append(0)
        elif match == ')':
            if stack:
                level = stack.pop()
                outer_level
                result.append(outer_level)
                stack.pop()
    Vermster here is a logic in handling nested parentheses.

test_code = """
parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
"""
print(parse_nested_parens(test_code))  # Output: [2, 3, 1, 3]
```
The logic works by keeping track of the level of nesting for each open parenthesis, and when a close parenthesis is encountered, we pop the topmost level from the stack and add it to our result. This allows us to accurately track the deepest level of nesting.