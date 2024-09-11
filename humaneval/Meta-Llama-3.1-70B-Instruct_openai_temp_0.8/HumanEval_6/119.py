```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the results
    results = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the maximum nesting level and the current nesting level to 0
        max_nesting = 0
        current_nesting = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting level
            if char == '(':
                current_nesting += 1
                # Update the maximum nesting level if the current nesting level is greater
                max_nesting = max(max_nesting, current_nesting)
            # If the character is a closing parenthesis, decrement the current nesting level
            elif char == ')':
                current_nesting -= 1

        # Append the maximum nesting level for the group to the results list
        results.append(max_nesting)

    # Return the list of results
    return results

# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```