```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting for each group of parentheses in a given string.

    Args:
    paren_string (str): A string of groups of parentheses separated by spaces.

    Returns:
    List[int]: A list of deepest levels of nesting for each group of parentheses.

    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()
    
    # Initialize a list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Initialize a counter for the current nesting level
        nesting_level = 0
        # Initialize a flag to track if we are inside a group of parentheses
        inside_group = False
        
        # Initialize a stack to keep track of opening parentheses
        stack = []
        
        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # If we are not inside a group of parentheses, mark that we are now
                if not inside_group:
                    inside_group = True
            # If the character is a closing parenthesis
            elif char == ')':
                # If we are not inside a group of parentheses, raise an error
                if not inside_group:
                    raise ValueError("Unbalanced parentheses")
                # If the stack is empty, raise an error
                if not stack:
                    raise ValueError("Unbalanced parentheses")
                # Pop the opening parenthesis from the stack
                stack.pop()
                # If the stack is empty, we are no longer inside a group
                if not stack:
                    inside_group = False
                # Increment the nesting level
                nesting_level += 1
        # If the stack is not empty, there are unbalanced parentheses
        if stack:
            raise ValueError("Unbalanced parentheses")
        
        # The deepest level of nesting is the maximum we've seen so far, or the current nesting level if we've only seen this group
        results.append(max(nesting_level, 0))
    
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```