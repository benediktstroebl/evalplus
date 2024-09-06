```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function will return the deepest level of nesting of parentheses in the string.
    """
    The string will be passed in, and the function will return a list of the deepest level of nesting for each group of parentheses in the string.
    """
    list of the deepest level of nesting for each group of parentheses in the string.
    """
    list = []
    for i, char in enumerate(s):
        if char == '(':
            list.append(1)
        elif char == ')':
            list.append(len)
        else:
            pass
    return list

# Unit Tests
test_parse_nested_parens = []
test_parse_nested_parens.append('(())')
test_parse_nested_parens.append('(()())')
test_parse_nested_parens.append('((()))')
test_parse_nested_parens.append('()())')
test_parse_nested_parens.append('((()))()()()()()')
test_parse_nested_parens.append('()()()()())')
test_parse_nested_parens.append('(()())()()()()()()()')
test_parse_nested_parens.append('()()(()())()()()')
test_parse_nested_parens.append('()())()()()()(()')
```