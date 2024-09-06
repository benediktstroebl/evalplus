```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack: List[int] = []
    result = []
    for match in parenthes_str.match(r'([')([-,';]': ('|*') for _ in '([ ]+')]):
        stack.append(1)
        if match.group().match(')':
            stack.append(2)
        match.group(')': stack.append(3)
   match('):')
        result.append(stack.pop())
    test(')')
    return result
def test_parse_nested_parens():
    test_str = "(()()) ((())) () ((())()())"
    actual = parse_nested_parens(test_str)
    assert actual == [2, 3, 1, 3]
```
This script defines a function **`parse_nested_parens`** that parses a string representing nested parentheses. The function uses a **`re`** module to find and match parentheses in the string. The function then builds a stack of parenthesis levels and returns the deepest level of nesting found. The test function tests the string and compares the result with the expected output.