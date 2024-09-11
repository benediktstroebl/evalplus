```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input, 
    separated by spaces. It returns a list of integers representing 
    the maximum level of nesting for each group of parentheses.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[int]: A list of integers, where each integer represents the maximum level of nesting for a group of parentheses.
    """
    def max_nesting_level(paren_str: str) -> int:
        # Initialize a stack and a counter for the nesting level
        stack = 0
        max_level = 0
        
        # Iterate over the characters in the string
        for char in paren_str:
            # If the character is an opening parenthesis, push it onto the stack and increment the nesting level
            if char == '(':
                stack += 1
                max_level = max(max_level, stack)
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and decrement the nesting level
            elif char == ')':
                stack -= 1
        
        # Return the maximum nesting level
        return max_level

    # Split the input string into groups of parentheses and calculate the maximum nesting level for each group
    return [max_nesting_level(group) for group in paren_string.split()]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of integers representing the maximum level of nesting for each group of parentheses. The function uses a helper function `max_nesting_level` to calculate the maximum nesting level for each group. The `max_nesting_level` function uses a stack to keep track of the nesting level and returns the maximum nesting level found. The `parse_nested_parens` function splits the input string into groups of parentheses, calculates the maximum nesting level for each group using `max_nesting_level`, and returns the list of maximum nesting levels.