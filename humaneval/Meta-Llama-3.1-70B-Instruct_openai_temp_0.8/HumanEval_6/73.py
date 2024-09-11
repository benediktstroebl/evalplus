```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    """
    groups = paren_string.split()
    max_depths = []
    
    for group in groups:
        max_depth = 0
        current_depth = 0
        
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        # Check if the parentheses are balanced
        if current_depth!= 0:
            raise ValueError(f"Unbalanced parentheses in group: {group}")
        
        max_depths.append(max_depth)
    
    return max_depths


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces. It splits the input string into groups, then iterates over each group to calculate the maximum depth of nesting. The function uses a stack-like approach to keep track of the current depth of nesting, incrementing the depth when it encounters an opening parenthesis and decrementing it when it encounters a closing parenthesis. The maximum depth for each group is stored in a list, which is returned as the result. The script also includes a check to ensure that the parentheses in each group are balanced.