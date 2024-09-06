```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for c in s:
        if c == '(': stack.append(1)
        else:
            if not stack or stack[-1] == '(':
                stack.append(0)
            else:
                level = stack.pop()
                [max_level=len(stack)
                current_level=0
                nested_level = 0
                for _ in range(max_level):
                    if stack[current_level] == '(':
                        nested_level += 1
                    stack.append(1)
                else:
                        stack.append(0)
                current_level += nested_level
                stack.append(0)
                yield nested_level
        else:
            stack.append(0)
    else: stack.append(c)
    return stack


def test_parse_nested_parens(test_string: str) -> None:
    parsed = parse_nested_parens(test_string)
    if parsed:
        print("Test passed!")
    else:
        print("Test failed")
```

This script defines a function `parse_nested_parens` that parses a string of nested parentheses. The function uses a `stack` to keep track of the level of nesting, and it starts by appending the first character to the stack.

The `test_parse_nested_parens` function is used to test the `parse_nested_parens` function with a given test string. The function should print "Test passed!" If the test is successful, the output will be "Test passed!" and if the test fails, the output will be "Test failed."