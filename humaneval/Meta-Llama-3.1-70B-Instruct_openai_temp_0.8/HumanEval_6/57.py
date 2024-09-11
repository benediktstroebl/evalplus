```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nested parentheses in each group.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.
    
    Returns:
        List[int]: A list of integers representing the maximum depth of nesting for each group.
    """

    # Split the input string into groups
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group
    for group in groups:
        # Initialize the stack and the maximum depth
        stack = []
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, push it onto the stack
            if char == '(':
                stack.append(char)
                # Update the maximum depth if necessary
                max_depth = max(max_depth, len(stack))
            # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
            elif char == ')':
                stack.pop()

        # Append the maximum depth for this group to the results list
        results.append(max_depth)

    # Return the list of results
    return results


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```