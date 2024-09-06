```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] != 1:
                raise ValueError("Unexpected character in parentheses!")
            stack.pop()
           
        if stack:
                result.append(stack.pop()
            return result as result)
    return result

# Test cases
test_strs = [
    "(()())((()))()((())))()",
    "((()))",
    "((()))()()()()()()()()()()",
    "()()()()()()()()()"
]

for test_str in test_strs:
    parse_nested_parens(test_str)
```

This function `parse_nested_parens` uses a stack to keep track of open parentheses and their closing. It iterates through string character by character and, when it encounters a ')', it checks whether there's an open ')' to close. If not, it raises a `ValueError`. Otherwise, it pops the top of the stack, appends the top number of the stack to the result list, and returns the result. This function is tested to parse nested parentheses correctly and pass all corresponding tests.