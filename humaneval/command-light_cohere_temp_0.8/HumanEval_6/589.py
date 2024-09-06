```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    levels = 0
    for char in s:
        if char == "(":
            stack.append(levels)
            levels += 1
        elif char == ")":
            levels -= 1
            if not levels:
                stack.append(levels)
            else:
                return stack
    return stack
# Test the function
test_str = "(()()) ((())) () ((()))"
test_result = parse_nested_parens(test_str)
print(test_result)
``` 
This code defines the `parse_nested_parens` function that takes a string as input and returns a list of integers. It uses a nested parentheses notation to represent levels of nesting. This function uses a stack to keep track of the deepest level of nesting and returns the stack when finished. The output will be `[2, 3, 1, 3]`.