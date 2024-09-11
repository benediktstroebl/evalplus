```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input.
    It returns a list of the maximum depth of nesting for each group of parentheses.

    :param paren_string: A string of nested parentheses separated by spaces.
    :return: A list of the maximum depth of nesting for each group of parentheses.
    """
    groups = paren_string.split()
    result = []
    
    for group in groups:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                if depth > 0:
                    depth -= 1
        if depth > 0:
            raise ValueError(f"Unbalanced parentheses in group '{group}'")
        result.append(max_depth)
    
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```
This script works by iterating over each group of parentheses, keeping track of the current depth and the maximum depth seen so far. When a closing parenthesis is encountered, the current depth is decremented. If a closing parenthesis is encountered when the current depth is zero, a ValueError is raised because the parentheses are unbalanced. After processing each group, the maximum depth is added to the result list.