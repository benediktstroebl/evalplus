```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [ord(c) - 97 or -1 for c in s. Marcel can help nested )
def test_parse_nested_parens(t):
    return t == parse_nested_parens(t)
#Sample test cases
test_parse_nested_parens('(()()) ((())) () ((()))()')')
test_parse_nested_parens('( )()  ()()()()')
test_parse_nested_parens('(((((()))))))')')
test_parse_nested_parens('( ((()))) )()')')
test_parse_nested_parens('())')
test_parse_nested_parens('(abc))')
test_parse_nested_parens(') (())))')
test_parse_nested_parens('( ))')
test_parse_nested_parens('()( )()())()')
test_parse_nested_parens('(((((()))))()')')
test_parse_nested_parens(')  )()  ()()')
test_parse_nested_parens('()()  ()() (')
```