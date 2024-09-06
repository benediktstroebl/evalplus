```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for char in parent_string:
        if char == "(":
            stack.append(1)
        else:
            if not stack or char == ")":
                stack.pop()
            else:
                stack.append(0)
                result.push(stack[result)
    return result

def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((()))"[3, 3, 1, 3]
    )
    assert parse_nested_parens("(>>)"[(])>())"
    assert parse_nested_parens("(>>)>>") is []
    assert parse_nested_parens("())") is []
    assert parse_nested_parens("(((((())))))))))"))" == [4]
    assert parse_nested_parens("(((((((((((()))))))))))))))))))))" == [5]

def test_parse_nested_parens_results():
    assert parse_nested_parens("(()()) ((())) () ((()))"[3, 3, 1, 3]")" == [2, 3, 1, 3])

# Example usage:
test_parse_nested_parens()
```