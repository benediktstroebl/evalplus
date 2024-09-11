```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces
    and returns a list of the maximum depth of nesting for each group.

    Args:
    paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the maximum depth of nesting for each group.
    """
    def max_nesting(group: str) -> int:
        # Initialize the maximum nesting depth and the current nesting depth
        max_depth = 0
        curr_depth = 0
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase the current depth
            if char == '(':
                curr_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, curr_depth)
            # If the character is a closing parenthesis, decrease the current depth
            elif char == ')':
                curr_depth -= 1
        
        # Return the maximum nesting depth
        return max_depth

    # Split the input string into groups and return the maximum nesting depth for each group
    return [max_nesting(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that calculates the maximum nesting depth for each group of nested parentheses in the input string. The function uses a helper function `max_nesting` to calculate the maximum nesting depth for each group. The `max_nesting` function iterates over each character in the group, keeping track of the current nesting depth and updating the maximum depth as necessary. Finally, the script tests the function with the provided example input.