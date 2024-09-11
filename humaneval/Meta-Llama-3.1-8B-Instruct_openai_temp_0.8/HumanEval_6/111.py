```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string of nested parentheses and return a list of the deepest level of nesting for each group.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum nesting levels
    max_nesting_levels = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize counters for opening and closing parentheses
        opening_count = 0
        max_opening = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the opening count
            if char == '(':
                opening_count += 1
                # Update the maximum opening count
                max_opening = max(max_opening, opening_count)
            # If the character is a closing parenthesis, decrement the opening count
            elif char == ')':
                opening_count -= 1

        # Append the maximum nesting level for the group to the list
        max_nesting_levels.append(max_opening)

    # Return the list of maximum nesting levels
    return max_nesting_levels

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of nesting for each group. It uses a simple iterative approach to count the opening and closing parentheses in each group and keeps track of the maximum opening count (i.e., the deepest level of nesting). The function is then tested with the example input provided in the problem statement.