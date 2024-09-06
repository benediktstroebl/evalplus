```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []

    for char in parent_string:
        if char == "(":
            stack.append(0)
        elif char == ")":
            if stack:
                open_level, close_level = stack.pop()
                deepest = len(stack)
                output.append(deepestest)
                stack.append(close_level + 1)
        else:
            stack.append(char)

    return output


def test_parse_nested_parens(test_string: str) -> None:
    parsed_output = parse_nested_parens(test_string)
    if parsed_output != [2, 3, 1, 3]:
        print("Test failed")
        return None

    print("Test passed")
    return None
```