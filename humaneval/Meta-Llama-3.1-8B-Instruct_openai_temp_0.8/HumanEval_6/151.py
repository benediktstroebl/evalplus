```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input, 
    separated by spaces. It returns a list of the maximum level of 
    nesting for each group of parentheses.

    Args:
    paren_string (str): A string of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of the maximum level of nesting for each group of parentheses.
    """
    
    def max_depth(s: str) -> int:
        """
        This helper function calculates the maximum depth of nesting for a given string of parentheses.
        
        Args:
        s (str): A string of nested parentheses.
        
        Returns:
        int: The maximum level of nesting for the given string of parentheses.
        """
        max_depth = 0  # initialize maximum depth
        current_depth = 0  # initialize current depth
        
        for char in s:  # iterate over each character in the string
            if char == '(':  # if the character is an opening parenthesis
                current_depth += 1  # increase the current depth
                max_depth = max(max_depth, current_depth)  # update maximum depth if necessary
            elif char == ')':  # if the character is a closing parenthesis
                current_depth -= 1  # decrease the current depth
        
        return max_depth  # return the maximum depth

    groups = paren_string.split()  # split the input string into groups of parentheses
    return [max_depth(group) for group in groups]  # calculate and return the maximum depth for each group

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input, separated by spaces. It uses a helper function `max_depth` to calculate the maximum level of nesting for each group of parentheses. The `max_depth` function iterates over each character in the string, incrementing or decrementing the current depth as it encounters opening or closing parentheses. The maximum depth encountered is used to update the overall maximum depth. Finally, the script demonstrates the usage of the `parse_nested_parens` function with an example input string.