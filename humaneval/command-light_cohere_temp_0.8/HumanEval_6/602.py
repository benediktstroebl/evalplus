```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    in_string = False  # Flag to track if we are inside a string
    for c in s:
        if in_string and c == ' ':
            stack.append(1)
            in_string = False  # Clear the flag after each space to start a new group
        elif in_string:
            in_string = False  # Start a new group if not inside a string
            result.append(stack.pop())
        stack.append(c)
        in parentheses or brackets.

def test_parse_nested_parens():
    test_string = "(()()) ((())) () ((()))"
    assert parse_nested_parens(test_string) == [2, 3, 1, 3]

# Run the tests
test_parse_nested_parens()  # This will fail initially, as the function doesn't execute correctly due to missing import.