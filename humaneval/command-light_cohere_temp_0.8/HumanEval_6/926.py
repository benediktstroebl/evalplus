```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    ret = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                ret.append(0)
            stack.append(0)
        else:
                ret.append(stack.pop()[0] + 1)
                stack.append(0)
    return ret
def test_parse_nested_parens(input_str: str) -> None:
    assert parse_nested_parens(input_str) == [1, 3, 2, 3]
``` 
This code implements a function `parse_nested_parens` that takes a string of nested parentheses and returns a list of the deepest level of nesting for each group of parentheses. 
It uses a stack data structure to keep track of opening parentheses and the most recent closing parentheses, and the `ret` list to store the results of parsing. 

The `test_parse_nested_parens` function is a simple assertion that the `parse_nested_parens` function correctly parses the input string.