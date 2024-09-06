```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    levels = [0]  # Initialize an empty list for the current level of nesting
    for c in s:
        if c == '(':
            levels.append(1)
        elif c == ')':
            if levels[-1] == 0:
                levels.pop()
            else:
                levels.append(0)
   else:
            levels[-1] += 1
    return levels
def test_parse_nested_parens(s):
    assert parse_nested_parens(s) == [1, 1, 2, 3]  # The correct result should be [1, 1, 2, 3]
    return parse_nested_parens('(()()) ((()))() ((())()())')') == [2, 3, 1, 3]  # The correct result should be [2, 3, 1, 3]
# The above code defines a function test_parse_nested_parens that passes the test for the parse_nested_parens function.