```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_level = 0
    output = []

    for char in s:
        if char == '(':
            opening_level += 1
        elif char == ')':
            if stack:
                stack.length = len(stack)
                opening_level -= 1
                if opening_level < 0:
                    output.insert(stack.pop(-opening_level)
                    output.insert(1)
                return output
            else:
                stack.push(opening_level)

    return output

# Test
def test_parse_nested_parens():
    test_string = "(()()) ((())) () ((()))"
    expected_output = [2, 3, 1, 3]
    parse_nested_parens(test_string)
    assert expected_output == parse_nested_parens(test_string)

# Run the test function and see if the test passes.