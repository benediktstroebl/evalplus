```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()', '))'):
        stack = [0]
        level = 0
        for c in s:
            if c == opener:
                stack.append(level)
                level += 1
            elif c == closer:
                level -= 1
                stack.append(level)
        result.append(stack.pop())
    return result
```

The approach employs a stack to keep track of the level of nesting for each opening parenthesis encountered. Whenever an opening parenthesis is found, the current level is recorded on the stack, and it is incremented. On encountering a closing parenthesis, the level is decremented, and the updated level is pushed onto the stack. To ensure the correct level is recorded, the last value popped from the stack corresponds to the deepest level of nesting for each group.

The test cases are designed to cover various scenarios, including edge cases, to ensure the function behaves as expected:
```python
def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("(()") == [1]
    assert parse_nested_parens("())") == [1]
    assert parse_nested_parens("(()()))") == [2, 1]
    assert parse_nested_parens("()()()") == [1]
```