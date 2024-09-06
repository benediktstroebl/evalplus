```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(3)
            stack.append(0)
        else:
                stack[-1] += 1
    return result
#Test cases
test_cases = [
    "(()()) ((())) () ((())()())",
    "())",
    "((()))"
]
for case in test_cases:
    actual = parse_nested_parens(case)
    expected = [2, 3, 1, 3]
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"
```
This code defines a function `parse_nested_parens` that parses and returns the deepest level of nesting for a given string of parentheses. It uses a type hints, such as `List` for the function parameters and return types, and the function uses a stack to keep track of open parentheses. The function then iterates over the characters in the input string, and for each character, it checks if it's an open parenthesis, in which case it adds 1 to the stack, and if it's a close parenthesis, it adds 0 to the stack, which effectively finds the depth of nesting. The function returns a level of nesting of the closed parentheses.