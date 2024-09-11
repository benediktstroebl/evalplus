```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses 
    in each group of parentheses separated by spaces.

    Args:
        paren_string (str): A string containing multiple groups of 
            nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of 
            nesting for each group of parentheses.
    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize a list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize a stack to keep track of the nesting level
        stack = []
        # Initialize the maximum nesting level for this group
        max_nesting = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Update the maximum nesting level if necessary
                max_nesting = max(max_nesting, len(stack))
            # If the character is a closing parenthesis, pop the corresponding 
            # opening parenthesis from the stack
            elif char == ')':
                stack.pop()

        # Append the maximum nesting level for this group to the results
        results.append(max_nesting)

    # Return the list of maximum nesting levels for all groups
    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```