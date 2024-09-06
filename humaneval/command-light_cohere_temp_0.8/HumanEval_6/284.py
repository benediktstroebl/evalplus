```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if not stack or stack[-1] == 3:
                output.append(stack.pop()
            append 1)
            stack. 
    return output
 
def test_parse_nested_parens(input_str: str) -> None:
    assert parse_nested_parens("((())) ((())) () ((()))()") == [2, 3, 1, 3])
```
This code defines a function **parse_nested_parens** that parses a string of nested parentheses and returns a list of the deepest nesting levels. The function uses a stack data structure to keep track of open parentheses. It starts with the input string, and iterates over each character. It adds characters to the stack if they are open parentheses "(" or ) and pushes them back if they are close parentheses ")." It keeps track of the deepest nesting level by checking the last character in the stack and only pushes back a 3 if it is the last character. The **test_parse_nested_parens** function tests this function with a sample input string and ensures that the output of the parse_nested_parens function is correct.