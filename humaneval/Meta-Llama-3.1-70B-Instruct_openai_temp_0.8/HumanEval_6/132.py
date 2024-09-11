```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers where each integer represents the deepest level of nesting of parentheses in each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting of parentheses in each group.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum nesting levels
    max_nesting_levels = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the maximum nesting level and the current nesting level to 0
        max_nesting_level = 0
        current_nesting_level = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current nesting level
            if char == '(':
                current_nesting_level += 1
                # Update the maximum nesting level if the current nesting level is greater
                max_nesting_level = max(max_nesting_level, current_nesting_level)
            # If the character is a closing parenthesis, decrement the current nesting level
            elif char == ')':
                current_nesting_level -= 1

        # Append the maximum nesting level to the list
        max_nesting_levels.append(max_nesting_level)

    # Return the list of maximum nesting levels
    return max_nesting_levels


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```