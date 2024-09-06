```python
def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    output = []
    for char in paren_string:
        if char == ')':
            stack.append(len)  # to stack
        elif char == '(':
            if len(stack) == 0:
                output.append(1)  # empty parent
            else:
                stack.append(stack.pop())  # out the core
        and the stack.pop() and stack,
    output.append(len))
    return output

def test_parse_nested_parens() -> None:
    # Test case 1
    test_cases = [
        "(()()) ((())) () ((()))",
        "(()()) ((())()())",
        "((())()()()())()()()()()())",
        "((())()) ((())()()())",
        "((())()) (())()())",
        "()()()()()()()()()"
    ]

    # Test case 2
    for test in test_cases:
        parsed = parse_nested_parens(test)
        assert parsed == [2, 3, 1, 3]

    # Test case 3
    for test in test_cases:
        parsed = parse_nested_parens("""
        (A()) (B())
        """)
        assert parsed == [1, 3]

    # Test case 4
    for test in test_cases:
        parsed = parse_nested_parens("""
        (()) (())
        """)
        assert parsed == [1]

    return None  # test completed
```