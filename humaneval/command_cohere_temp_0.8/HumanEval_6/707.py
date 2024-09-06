Here's a Python script with a self-contained function that solves the problem using a nested dictionary to keep track of the maximum depth for each group of parentheses:
```python
from typing import List, Dict

def parse_nested_parens(paren_string: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses.
E.g. (()()) has maximum two levels of nesting while ((())) has three.

Args:
    paren_string (str): String with multiple groups of nested parentheses separated by spaces.

Returns:
    List[int]: List that contains deepest nesting level for each group of parentheses.
"""
    if not paren_string:
        return []

    # Split the string into individual groups of parentheses
    paren_groups = paren_string.split()
    max_depths = []  # List to store maximum depths for each group

    for paren_group in paren_groups:
        # Use a dictionary to keep track of the maximum depth for each opening parenthesis
        group_depth = {}

        # Iterate over each character in the current group
        for char in paren_group:
            if char == '(':
                group_depth[char] = group_depth.get(char, 0) + 1
            else:
                if char in group_depth:
                    group_depth[char] -= 1

        # Get the maximum depth from the nested dictionary
        max_depth = max(group_depth.values())
        max_depths.append(max_depth)

    return max_depths
```
The provided example in the docstring and the test case are also included to demonstrate the function. The function will return a list where each element corresponds to the deepest level of nesting for the respective group of parentheses. 
This approach uses a nested dictionary to keep track of the opening parentheses and determines the maximum depth by iterating over the characters in each group.