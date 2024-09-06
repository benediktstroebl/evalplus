```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(': stack.push(len)
        elif c == ')': stack.pop()
        result.append(level)
   while c == ')'
  return result
#Test cases 
test_case1 = parse_nested_parens('(()()) ((())) () ((())()())')
test_case2 = parse_nested_parens('()()()  ()')
test_case3 = parse_nested_parens('((()))()()()')
test_case4 = parse_nested_parens('() ((())))()')
test_case5 = parse_nested_parens('()() ()( )')
test_case6 = parse_nested_parens('( )( )()()())')
test_case7 = parse_nested_parens('(( )()()() )()')
test_case8 = parse_nested_parens('() ( )  ( )()()')
test_case9 = parse_nested_parens('()( ( ) )()')
test_case10 = parse_nested_parens('()  ()()()')
test_case11 = parse_nested_parens('() ( )())'

def test_function_parse_nested_parens(testcase: str) -> None:
    parse_nested_parens(testcase)
 
for testcase in [test_case1, test_case2, test_case3, test_case4, test_case5, test_case6, test_case7, test_case8, test_case9, test_case10, test_case11]:
    test_function_parse_nested_parens(testcase)
``` 
This code defines a function `parse_nested_parens` that takes a string as input and returns a list of integers. The function uses a levels of nesting while ( ) has three levels, and pushes the deepest level of nesting onto a stack. The loop iterates over each character, and if it's an opening parenthesis, pushes it onto the stack. If it's closing parenthesis, pops it from the stack and appends it to the result list.