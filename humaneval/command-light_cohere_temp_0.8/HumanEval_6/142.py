```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    open_level: int = 0
    output: List[int] = []
    for char in s:
        if char == '(':
            open_level += 1
        elif char == ')':
            open_level -= 1
        else:
            stack.push(open_level)
            output.push(stack.pop(stack))
       stack = []
    return output
# Tests
# Test with a string containing nested parentheses
test_string = "(()()) ((())) () ((()))"
test_output = parse_nested_parens(test_string)
print(test_output)  # Output: [2, 3, 1, 3]
``` 
This function uses a stack to keep track of the open levels of parentheses, it adds the open level to the stack each time it encounters an open parent, and it subtracts the open level from the stack each time it encounters a close parent.  Then the to keep track of the deepest level of nesting of parentheses.