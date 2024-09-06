```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack = []
    in_nesting = False
    opening_level = 0
    levels = []

    for char in parenthes_str:
        if char == "(":
            if not in_nesting:
                stack.append(opening_level)
                in_nesting = True
            opening_level += 1
        elif char == ")":
            if in_nesting:
                stack.append(opening_level)
                in_nesting = False
            opening_level -= 1
        elif in_nesting:
            stack.append(opening_level)

        levels.append(stack.pop())
    final_ level, starting with opening_level

    return levels
def test_function():
    assert parse_nested_parens("(()()) ((())) () ((()))()") == [2, 3, 1, 3], "test failed"
    assert parse_nested_parens("(()()()())") == [1, 2], "test failed"
    assert parse_nested_parens("(()())") == [1], "test failed"
    assert parse_nested_parens("((()))") == [2], "test failed"
    assert parse_nested_parens("(()()) ()") == [1, 2], "test failed"
```
The `test_function` adds some tests for `parse_nested_parens` function. The function asserts that the test with correct values.