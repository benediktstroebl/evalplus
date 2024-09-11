```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers representing the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting for each group.
    """

    # First, we split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum nesting levels
    max_nesting_levels = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the current nesting level and the maximum nesting level for this group
        curr_nesting_level = 0
        max_nesting_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting level
            if char == '(':
                curr_nesting_level += 1
                # Update the maximum nesting level if necessary
                max_nesting_level = max(max_nesting_level, curr_nesting_level)
            # If the character is a closing parenthesis, decrement the current nesting level
            elif char == ')':
                curr_nesting_level -= 1

        # Append the maximum nesting level for this group to the list
        max_nesting_levels.append(max_nesting_level)

    # Return the list of maximum nesting levels
    return max_nesting_levels


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script first splits the input string into groups of parentheses, then iterates over each group to calculate its maximum nesting level. The maximum nesting level for each group is calculated by keeping track of the current nesting level as we iterate over the characters in the group, and updating the maximum nesting level whenever the current nesting level exceeds it. The script finally returns a list of the maximum nesting levels for all groups.