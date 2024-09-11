```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the maximum depth of nested parentheses for each group in a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the maximum depth of each group of parentheses.
    """

    # Split the input string into groups of parentheses
    groups = paren_string.split()

    # Initialize an empty list to store the maximum depth of each group
    max_depths = []

    # Iterate over each group of parentheses
    for group in groups:
        # Initialize the current depth and maximum depth to 0
        curr_depth = 0
        max_depth = 0

        # Iterate over each character in the group
        for char in group:
            # If the character is an opening parenthesis, increment the current depth
            if char == '(':
                curr_depth += 1
                # Update the maximum depth if the current depth is greater
                max_depth = max(max_depth, curr_depth)
            # If the character is a closing parenthesis, decrement the current depth
            elif char == ')':
                curr_depth -= 1

        # Append the maximum depth of the current group to the list
        max_depths.append(max_depth)

    # Return the list of maximum depths
    return max_depths


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

In this script, the `parse_nested_parens` function first splits the input string into groups of parentheses using the `split` method. Then, for each group, it iterates over each character, keeping track of the current depth and maximum depth. The current depth is incremented when an opening parenthesis is encountered and decremented when a closing parenthesis is encountered. The maximum depth is updated whenever the current depth exceeds it. Finally, the function returns a list of the maximum depths for each group of parentheses.