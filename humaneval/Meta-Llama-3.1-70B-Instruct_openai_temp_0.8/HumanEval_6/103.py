```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses 
    separated by spaces and returns a list of the deepest level of nesting 
    for each group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses 
                             separated by spaces.

    Returns:
        List[int]: A list of the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # split the input string into groups
    max_levels = []  # initialize a list to store the maximum levels

    for group in groups:
        max_level = 0  # initialize the maximum level for the current group
        current_level = 0  # initialize the current level

        for char in group:
            if char == '(':  # if the character is an opening parenthesis
                current_level += 1  # increase the current level
                max_level = max(max_level, current_level)  # update the maximum level
            elif char == ')':  # if the character is a closing parenthesis
                current_level -= 1  # decrease the current level

        max_levels.append(max_level)  # append the maximum level to the list

    return max_levels


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script uses a simple iterative approach to parse each group of nested parentheses. It keeps track of the current level of nesting and the maximum level encountered so far for each group. The maximum levels are then returned as a list. The time complexity of this script is O(n), where n is the total number of characters in the input string.