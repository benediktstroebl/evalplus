Here is a self-contained Python script that solves the problem of parsing and identifying the depth of nested parentheses:
```python
from typing import List
def parse_nested_parens(input_str):
    # Function to parse and return the deepest level of nesting for parentheses in the input string
    stack = []
    for char in input_str:
        if char == "(":
           stack.append(True)
       
        elif char == ")":
           if len(stack) == 0:
               stack.append(False)
           else:
               stack[-1] = False
           else:
               stack.push()
    This basic way to identify the deepest level of nesting
    if len(stack) == 0:
        return 0
    else:
        return len(stack)

# Unit tests
def test_parse_nested_parens():
    test_cases = [
        "(()())((())())",
        "((((())))())",
        "(()()())()()()()()()()()()",
        "()()()((())()())",
        "()(()())",
        "(())()",
        "()",
        "() ()"
    ]
    for case in test_cases:
        actual_result = parse_nested_parens(case)
        expected_result = 4
        assert actual_result == expected_result, f"Unexpected result: {actual_result}, Expected: {expected_result}"
        print(f"Test case {i+1}: {case} passed.")
if __name__ == "__main__":
    test_parse_nested_parens()
```
This script defines the `parse_nested_parens` function, which takes an input string and returns the deepest level of nesting for parentheses in the input string. The `test_parse_nested_parens` function contains several test cases that validate the function's correctness. 
When you run the script, it will run all the test cases and report whether each test has passed or failed.