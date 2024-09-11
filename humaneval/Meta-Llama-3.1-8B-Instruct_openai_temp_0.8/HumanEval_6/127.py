```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input, 
    where each group of parentheses is separated by spaces.
    It returns a list of the maximum depth of parentheses for each group.

    Args:
        paren_string (str): A string of nested parentheses.

    Returns:
        List[int]: A list of maximum depths of parentheses for each group.
    """
    paren_string = paren_string.split()
    result = []
    
    for group in paren_string:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
                if depth < 0:
                    raise ValueError("Unbalanced parentheses")
        if depth!= 0:
            raise ValueError("Unbalanced parentheses")
        result.append(max_depth)
    
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, splits it into groups, and calculates the maximum depth of nesting for each group. The function then returns a list of these maximum depths. The script also includes a test case to demonstrate the function's usage.