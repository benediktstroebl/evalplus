```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    open_braces = []
    result = []

    for char in parent_string:
        if char == "(":
            if not in open_braces:
                stack.append(1)
                open_braces.append(char)
        else:
                open_braces.append(char)
        else:
            if char == ")":
                stack.pop()
                stack[-1]
                open_braces.append(char)
            else:
                stack.append(char)
            continue
        else:
            result.append(stack.pop()
            return int, - len(stack)
        return result

    # Test
    test_cases = [
        "(()()) ((())) () ((())())",
        "()()()((())()())",
        "((()))",
        "()((())))"
    ]
    for case in test_cases:
        actual = parse_nested_parens(case)
        expected = [2, 3, 1, 3]
        assert actual == expected, f"Actual: {actual}, Expected: {expected}"
```
The above code defines a function parse_nested_parens that takes a string of nested parentheses as input and returns a list of integers representing the deepest level of nesting for each group. The code uses a stack and open_braces to keep track of the open and closed parentheses respectively.