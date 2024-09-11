```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It calculates the deepest level of nesting of parentheses for each group and returns them as a list.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of deepest level of nesting of parentheses for each group.
    """

    def count_parens(s: str) -> int:
        """ Helper function to count the deepest level of nesting of parentheses in a string. """
        
        # Initialize counters for opening and closing parentheses
        open_count = 0
        max_count = 0
        
        # Iterate over each character in the string
        for char in s:
            # If it's an opening parenthesis, increment the counter
            if char == '(':
                open_count += 1
                # Update the maximum counter if necessary
                max_count = max(max_count, open_count)
            # If it's a closing parenthesis, decrement the counter
            elif char == ')':
                open_count -= 1
        
        # Return the maximum counter value
        return max_count

    # Split the input string into groups and count the deepest level of nesting for each group
    groups = paren_string.split()
    result = [count_parens(group) for group in groups]
    
    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces as input and returns a list of deepest level of nesting of parentheses for each group. It uses a helper function `count_parens` to count the deepest level of nesting of parentheses in a string. The main function splits the input string into groups, counts the deepest level of nesting for each group, and returns the results as a list.