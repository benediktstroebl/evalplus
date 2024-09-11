```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting of parentheses for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting of parentheses for each group.
    """
    
    def max_depth(s: str) -> int:
        """
        Helper function to calculate the maximum depth of nesting of parentheses in a string.

        Args:
            s (str): A string of nested parentheses.

        Returns:
            int: The maximum depth of nesting of parentheses in the string.
        """
        depth = 0
        max_depth = 0
        
        for char in s:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1
        
        # If the number of opening parentheses is not equal to the number of closing parentheses,
        # it means the string is not a valid representation of nested parentheses.
        if depth!= 0:
            raise ValueError("Invalid input string")
        
        return max_depth

    # Split the input string into groups and calculate the maximum depth of nesting for each group
    groups = paren_string.split()
    result = [max_depth(group) for group in groups]
    
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script first defines a helper function `max_depth` to calculate the maximum depth of nesting of parentheses in a string. It then uses this helper function to split the input string into groups and calculate the maximum depth of nesting for each group. The result is a list of the maximum depth of nesting for each group. The script includes a test case to demonstrate its usage.