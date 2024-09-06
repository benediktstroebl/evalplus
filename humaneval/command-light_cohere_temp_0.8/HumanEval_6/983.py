```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for char in parent_string:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                result.append(stack.pop()
                done.append(0))
            stack.append(char)
    done = True
        if not done:
            continue
        return result

def test_parse_nested_parens(test_string: str) -> None:
    assert parse_nested_parens(test_string) == [1, 3, 2, 3]
```
This code defines the function parse_nested_parens that takes a string as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. The function uses a stack to keep track of the open parentheses encountered and their corresponding closed versions. The result of the function is then compared with the test_string using the assert statement, which passes the test if the two values are equal.