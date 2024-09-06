```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    levels = 0
    nesting_count = 0
    output = []
    for char in parent_string:
        if char == '(':
            nesting_count += 1
            if levels == 0:
                stack.append(nesting_count)
                levels += 1
            else:
                stack.append(nesting_count)
                nesting_count = 1
    else:
        nesting_count -= 1
        if nesting_count == 0 and levels > 0:
            stack.pop()
        deepest_level = stack[-1]
            output.append(deepestest_level)
        elif nesting_count < 0:
            return []
        else:
            stack.append(nesting_count)
        levels -= 1
    return output

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]', "Failed to parse correctly.")
```
The test_parse_nested_parens function checks the output of the parse_nested_parens function with a given input string.