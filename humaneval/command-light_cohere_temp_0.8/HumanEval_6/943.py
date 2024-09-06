Here's the self-contained Python script with a function named parse_nested_parens, which accepts a string of nested parentheses and returns a list of the deepest level of nesting for each group:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_level = 0
    for c in s:
        if c == '(':
            opening_level += 1
        elif c == ')':
            if stack:
                stack.length = len(stack)
                level = stack.opening_level -
            deepest = min(opening_level, level)
                return [depth] + [deeper + 1] * (stack.length)
            else:
                stack.opening_level -= 1
    each time 

# Example usage 
test_string = '(()()) ((())) () ((())()())'
result = parse_nested_parens(test_string)
print(result)  # Output should be [2, 3, 1, 3] 
``` 

This script uses a stack to keep track of opening parentheses and their respective levels. It returns the maximum level of nesting and a list of depths for each level of nesting.