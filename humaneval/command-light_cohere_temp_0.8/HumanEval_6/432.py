```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    res = []
    for c in parent_string:
        if c == '(': stack.push(1)
        elif c == ')':
            if stack:
                res.pop()
               pop(...)
                stack.pop()
       if (1)
            stack.push(0)
        elif c == '(': stack.push(3)
        elif c == ')': stack.pop()
       pop() and stack.pop()
       pop() and stack.push(2)
    elif c == '(': stack.push(4)
    elif c == ')': stack.pop()
   pop() and stack.pop()
   pop()
   pop() and stack.pop()
   pop() and stack[-1]
    return res

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))()')' == [2, 3, 1, 3])

```
This code defines a function **`parse_nested_parens`** that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group of parentheses in the string. It then defines a test_parse_nested_parens function that asserts the function's output for a given input string is correct.