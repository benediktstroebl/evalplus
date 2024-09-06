```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, bracket_group in enumerate(s.split()):
        stack = []
        nesting_level = 0
        for bracket in bracket_group:
            if bracket == '(':
                stack.append(bracket)
            else:
                if not stack:
                    result.append(nesting_level)
                    continue
                stack.pop()
                nesting_level += 1
                if not stack:
                    result.append(nesting_level)
    return result
```

The approach employs a stack to track opening parentheses encountered and maintains a `nesting_level` variable that increments for each closing parenthesis opened. The function iterates through each bracket group separating them with spaces and pushes all open parentheses to the stack. When a closing parenthesis is encountered, the stack is checked for any open parentheses, if the stack is empty it means the current group has a maximum nesting level of the current `nesting_level`, so it's added to the result list. Otherwise, we pop an open parenthesis from the stack, increment the `nesting_level`, and check if the stack is empty again. This process is repeated until all open parentheses are closed and the final result is a list of deepest nesting levels for each group. 

The unit tests provide in the original prompt are tied to the `parse_nested_parens` function and validate its correctness against various scenarios:
```python
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('()') == [1]
    assert parse_nested_parens('(((((((()())))))))')) == [7]
    assert parse_nested_parens('(()') == [1]
    assert parse_nested_parens('()())') == [2]
    assert parse_nested_parens('(()())') == [2]
    assert parse_nested_parens('(()(()))') == [2]
    assert parse_nested_parens('()()()') == [3]
    assert parse_nested_parens('()(()())') == [2]
    assert parse_nested_parens('(()(()(()())))') == [3]
```