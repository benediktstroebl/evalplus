```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    open_levels = 0

    for c in s:
        if c == '(':
            open_levels += 1
            stack.append(open_levels)
        elif c == ')':
            open_levels -= 1
            if not open_levels:
                stack.append(0)
            elif open_levels < 0:
                stack.append(open_levels)
        else:
                stack.append(open_levels)
                open_levels = 0

    return stack

def test_parse_nested_parens(test_str: str) -> None:
    # Test 1
    assert parse_nested_parens('(())') == [2, 0]
    # Test 2
    assert parse_nested_parens('((()))') == [3, 0]
    # Test 3
    assert parse_nested_parens('(()())') == [1, 3]
    # Test 4
    assert parse_nested_parens('(()()) (())') == [1, 3, 1]
    return None
```