```python
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []

    for match in parentheses_string.match(r'\((.*?)\))'):  # match matches a group of parentheses
        content = match.group(0)  # match.group0 is match the match(')') if not stack or match.group('') else match

        stack.append(1)  # append to the stack
        stack.append(2)  # append to the stack

    stack.pop(0)  # pop the last element from the stack
    stack.append(3)  # append the deepest level of nesting

    while stack:
        result.append(stack.pop(0))  # append the maximum number of each group to the result

    return result

# Test cases
def test_parse_nested_parens():
    test_cases = [
        "(()()) ((())) () ((())())",",
        "((()))",
        "(())) () ((())()())",
        "()() () () ((())",
        "((())()())",
        "() ((())()) ()",
        "()() (()) ()"
    ]

    expected_results = [
        [2, 3, 1, 3],
        [3],
        [1],
        [3],
        [1, 2],
        []
    ]

    for test_case, expected_result in zip(test_cases, expected_results):
        result = parse_nested_parens(test_case)
        assert result == expected_result, f"Test case [{test_case}] failed."

test_parse_nested_parens()
```
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group. The `test_parse_nested_parens` function has a list of test cases with different strings of parentheses. Each test case starts by parsing the string and building the list of the deepest levels of nesting for each group. The function then compares the results with the expected results and asserts the correctness of the function's output for each test case.