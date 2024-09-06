```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    res = []
    start = 0
    for i, char in enumerate(s):
        if char == "(":
            stack.append(start)
        start = i + 1
        elif char == ")":
            if not empty_block():
                stack.pop()
           
                res.append(start)
            start = i + 1
        elif char == " ":
            stack.append(start)
        start = i + 1
        else:
            stack.append(char)
    res.append(char)
    return res

def empty_block():
    return True

def test_parse_nested_parens():
    test_string = "(()()) ((())) () ((())()())"
    return parse_nested_parens(test_string) == [2, 3, 1, 3]
```