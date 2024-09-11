```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    For each group, it returns the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers where each integer represents the deepest level of nesting for each group.
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        max_depth = 0
        current_depth = 0

        for paren in group:
            if paren == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif paren == ')':
                current_depth -= 1
                if current_depth < 0:
                    raise ValueError("Invalid parentheses group")

        if current_depth!= 0:
            raise ValueError("Invalid parentheses group")

        result.append(max_depth)

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```

This script defines the `parse_nested_parens` function as specified. It splits the input string into groups, then for each group, it iterates over the parentheses to calculate the maximum depth of nesting. The result is a list of integers, where each integer represents the deepest level of nesting for each group.

The script also includes a test case to demonstrate its functionality. If the input string contains any invalid parentheses groups (e.g., unmatched or improperly nested parentheses), the script raises a `ValueError`.