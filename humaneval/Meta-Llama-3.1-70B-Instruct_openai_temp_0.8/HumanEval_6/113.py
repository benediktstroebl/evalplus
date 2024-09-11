```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting for each group of parentheses in a given string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers, where each integer represents the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []
    
    for group in groups:
        max_depth = 0
        current_depth = 0
        
        for char in group:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        result.append(max_depth)
    
    return result

# Example usage
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```