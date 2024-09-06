```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                result.append(0)
            stack.append(0)
        else:
                result.append(stack.pop())
                return result list
    finished
    return result

# Unit Tests
def test_parse_nested_parens():
    test_string = """(()()) ((())) () ((())) () ((())) ()"""
    expected = [2, 3, 1, 3]
    actual = parse_nested_parens(test_string)
    assert actual == expected


# Main Execution
test_parse_nested_parens()
```
The provided Python code defines a function called `parse_nested_parens` that takes a string of nested parentheses as input and aims to return the deepest level of nesting. The function uses a stack to keep track of open parentheses and their depths. It iterates through characters in the string, opening parentheses push the depth to 1, and closing parentheses pop the depth back to 0. The process continues until no more parentheses are found, at which point, the function adds the deepest nesting level to the result list.