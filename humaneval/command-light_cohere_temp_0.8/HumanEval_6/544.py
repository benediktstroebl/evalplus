```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    open_level = 0
    for char in s:
        if char == '(':
            open_level += 1
        elif char == ')':
            open_level -= 1
        elif open_level == 0:
            stack.append(char)
        else:
            raise ValueError("Incorrect string format")
    return stack
# Unit tests
def test_parse_nested_parens():
    test_strs = [
        "(()())((())) ()((())()())",
        "((((()))))"",
        "((())))"
    ]
    for s in test_strs:
        actual = parse_nested_parens(s)
        expected = [2, 3, 1, 3]  # correct output
        assert actual == expected
# Main execution
if __name__ == "__main__":
    test_parse_nested_parens()
```
The provided code defines a Python function `parse_nested_parens` that takes a string containing multiple groups of nested parentheses as input and aims to return the deepest level of nesting for each group. The function uses a `stack` to keep track of opening parentheses and keeps track of the current level of opening parentheses. It iterates over each characters in the input string and adds them to the stack accordingly. After processing all characters, the function checks if the current opening level is 0, which means that the last character is a closing parenthesis, so it pops the character from the stack and returns it. If the current opening level is not 0, it raises a `ValueError` with an appropriate error message.

The code also includes unit tests for the `parse_nested_parens` function using the `test_strs` list, which contains different test cases. The `main` block demonstrates how to execute these unit tests.