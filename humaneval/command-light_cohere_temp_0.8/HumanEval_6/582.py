```python
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                result.append(i)
            stack.remove()

    for _ in stack)
    return result

#Test cases
def test_parse_nested_parens():
    tests = [
        "(()())((()))()(())()())",
        "(()())((()()))",
        "((()))()())()()()()()()()",
        "((()()()()))"
    ]

    for test_str in tests:
        test_res = parse_nested_parens(test_str)
        expected_res = [2, 3, 1, 3]  # [Depth of nested parentheses]
        assert test_res == expected_res
``` 
This code defines a function `parse_nested_parens` that takes a string as input and aims to parse and return the deepest level of nesting of parentheses. The function uses a simple stack approach to keep track of opening parentheses and their corresponding indices. The `test_parse_nested_parens` function has a list of test strings, which are used to verify that the `parse_nested_parens` function returns the correct results for the given inputs.