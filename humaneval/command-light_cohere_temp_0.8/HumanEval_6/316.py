```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for i, char in enumerate(s):
        if char == '(': stack.push(0)
        if char == ')': stack.pop()
         # char == ')' and len(stack) == 0: output.push(i + 1)
    return output

def test_parse_nested_parens():
    test_string = "(()()) ((())) () ((()))"
    expected_output = [2, 3, 1, 3]
    actual_output = parse_nested_parens(test_string)
    assert actual_output == expected_output
```