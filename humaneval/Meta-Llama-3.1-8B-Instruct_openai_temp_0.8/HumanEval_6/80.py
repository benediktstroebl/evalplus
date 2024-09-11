### Nested Parentheses Parser
#### Parse the deepest level of nesting of parentheses in a given string
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.

    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    def max_nesting_level(s: str) -> int:
        # Initialize the maximum nesting level and current nesting level to 0
        max_level = 0
        curr_level = 0
        
        # Iterate through the string
        for char in s:
            # If the character is an opening parenthesis, increment the current level
            if char == '(':
                curr_level += 1
                # Update the maximum level if the current level is greater
                max_level = max(max_level, curr_level)
            # If the character is a closing parenthesis, decrement the current level
            elif char == ')':
                curr_level -= 1
        
        # Return the maximum nesting level
        return max_level

    # Split the input string into groups
    groups = paren_string.split()
    # Use a list comprehension to find the maximum nesting level for each group
    return [max_nesting_level(group) for group in groups]

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```