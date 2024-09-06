Here's the improved code with self-contained function and tests:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    def helper(group: str) -> List[int]:
        stack = []
        levels = 0
        in_string = False
        result = []
        for char in group:
            if char == '(':
                in_string = True
                stack.append(levels)
                levels += 1
            if char == ')':
                in_string = False
                stack.pop()
                if levels == 0:
                    result.append(levels)
        return result
        return helper(group)
    return helper(s)
def test_parse_nested_parens() -> None:
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens(') ((()()))') == [1]
    assert parse_nested_parens(') ((((())))'))') == [1]
    assert parse_nested_parens('() (())') == []
    assert parse_nested_parens('() () () ()') == []
    return
```
The code defines a function `parse_nested_parens` that takes a string as input and uses a helper function to recursively parse nested parentheses levels. The helper function uses a stack and levels to keep track of the current state. The deepest level of nesting is returned as a list of integers.

The `test_parse_nested_parens` function contains several assertions that check the correctness of the `parse_nested_parens` function with different input strings.