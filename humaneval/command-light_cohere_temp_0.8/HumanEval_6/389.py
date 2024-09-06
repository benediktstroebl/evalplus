```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for match in parentheses_string.match(r'\((.*?)\)(.*?)\)'):
        content = match.group(1)
        if content:
            stack.append(1)
            content = match.group(2)
        if content:
            stack.append(2)
            result.append(stack.pop())
        pop()
            stack and push(1)
    return result
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())')' == [2, 3, 1, 3])
    assert parse_nested_parens('((()))'))' == [1]
    assert parse_nested_parens('()()() ()') == []
```
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting parentheses. It uses the `match` to find all matches of the pattern and uses the `group()` function to get the content of each group, which is either an empty string (if it's a top level open parenthesis) or the content of the current group.

The `test_parse_nested_parens` function has additional assertions to test the correctness of the `parse_nested_parens` function.