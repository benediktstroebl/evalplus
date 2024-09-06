```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string of nested parentheses into a list of their deepest-level indices.

    Args:
        s (str): string to parse

    Returns:
        list of indices, each corresponding to the deepest level of nesting
    """
    indices = []  # Initialize empty list to store results
    stack = []  # Stack to track the opening parentheses
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            if not stack or char == ")":
                indices.append(i)
                stack.remove()  # add a stack

    return indices


def test_parse_nested_parens():
    """
    Tests the parse_nested_parens function with various input strings
    """
    # Test with sample cases
    test_cases = [
        "(()())((()))()((()))()",  # Full of four levels
        "(()()())()()((())()())",  # Three levels
        "(()())((())())()",  # Two levels
        "((())())()()",  # Two levels with one remaining parent
    ]

    for case in test_cases:
        parsed = parse_nested_parens(case)
        expected = [2, 3, 1, 3]  # Corresponding levels of nesting
        assert parsed == expected, f"Test case [{case}] failed with expected [{expected}] but got [{parsed}] instead"

test_parse_nested_parens()  # Call the test function
```
This Python script defines a function `parse_nested_parens` that parses a string of nested parentheses into a list of their deepest-level indices. It also includes a test_parse_nested_parens function to test the `parse_nested_parens` function with various input strings.