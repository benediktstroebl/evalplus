Here's a Python script with a self-contained function that solves the problem using a consistent and efficient algorithm:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    max_nesting = []
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # Count nesting level
            curr_nesting = len(stack)
            while stack and stack[-1] != '(':
                curr_nesting += 1
                stack.pop()
            stack.pop()
            
            if curr_nesting > max_nesting[-1]:
                max_nesting.append(curr_nesting)
        elif char == ' ':
            if stack:
                max_nesting.append(stack[-1])
                stack = []
        else:
            raise ValueError("Invalid character:", char)
    
    # Add final nesting level
    if stack:
        max_nesting.append(stack[-1])
    
    return max_nesting
```
This approach uses a stack to keep track of parentheses encountered and maintains a list `max_nesting` to which the maximum nesting level of each group is appended. Additionally, it handles variations in input where spaces between groups are included or not.

Here's how you can test this function using the test case provided:
```python
test_str = '(()()) ((())) () ((())()())'
expected = [2, 3, 1, 3]
result = parse_nested_parens(test_str)
print(f"Result: {result}")
print(f"Expected: {expected}")
``` 
The output will show the result and the expected output side-by-side for comparison. 

This function should efficiently handle various input scenarios, including multiple groups of parentheses and varying levels of nesting.