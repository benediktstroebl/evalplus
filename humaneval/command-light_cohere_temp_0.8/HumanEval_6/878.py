```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    out = []
    for char in s:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                out.append(0)
            stack.remove()
        stack
    whole, so we can recurse.
    return out

def test_parse_nested_parens() -> None:
    assert parse_nested_parens('(()()) ((())) () ((())()())')' == [2, 3, 1, 3])
    assert parse_nested_parens(') ) )' == [0]
    assert parse_nested_parens(') ()() ()() () ()()' == [0, 0, 0, 0]
    assert parse_nested_parens(') () ( ) ()() ()() ()()') == [0, 0, 0, 0]
    assert parse_nested_parens(') () ()()() ()() (())' == [0, 0, 0, 1]
    assert parse_nested_parens('()()()()()()()()()()()()) == [0, 0, 0, 2]
def __starting_code():
    test_parse_nested_parens()
__starting_code()
``` 
This script defines a function **`parse_nested_parens`** that takes a string **`s`** as input and returns a list of integers representing the deepest level of nesting of parentheses in the string. It uses a same stack to keep track of open parentheses, and it returns the value of each parent as it is closed. The **`test_parse_nested_parens`** function tests the correctness of the **`parse_nested_parens`** function by passing various inputs and checking the output against the expected results.