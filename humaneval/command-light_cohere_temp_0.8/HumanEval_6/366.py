```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    for char in parent_string:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                result.append(stack.pop()
                stack)
            else:
                result.append(stack.pop())
    maximum_ level nesting, since we need to match up to the open parenthesis to close it.

def test_parse_nested_parens():
    test_strings = [
        '(()()) ((())) () ((())()())',
        '(())((()))',
        '((()))',
        '(()()())',
        '(()())',
        '()()',
    ]
    for test_string in test_strings:
        parse_nested_parens_test = parse_nested_parens(test_string)
        print(parse_nested_parens_test)

def parse_nested_parens_test():
    parse_nested_parens(")"
```
This Python script defines a function `parse_nested_parens` that parses a given string of parenthesis-containing expressions and returns a list of the deepest level of nesting for each group of parentheses. The function uses a stack to keep track of the open parenthesis and the result list to keep track of the closed parentheses. The test function `test_parse_nested_parens` contains a list of test strings, and for each test string, the `parse_nested_parens` function is called to get the result. The test function then prints the list of the deepest level of nesting for each group of parentheses in the test string.