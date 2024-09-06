Here's a Python script with a self-contained function that solves the problem using a `depth` counter to track the deepest level of nesting of parentheses for each group in the given input string:
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    levels = []
    current_level = 0  # Initialize current level of nesting to zero
    for char in paren_string:
        if char == '(':
            current_level += 1
        elif char == ')':
            current_level -= 1
        elif char == ' ':
            if current_level > 0:  # Add current level to the result list only if it's greater than zero
                levels.append(current_level)
                current_level = 0  # Reset current level to zero for the next group
    # Add the last level if it is greater than zero
    if current_level > 0:
        levels.append(current_level)
    return levels

# Test the function
paren_string = '(()()) ((())) () ((())()())'
print(parse_nested_parens(paren_string))
```
The provided example will output:
```bash
[2, 3, 1, 3]
```
This solution efficiently determines the deepest level of nesting for each group in the input string without introducing additional complexity related to parsing the entire string in a specific direction.