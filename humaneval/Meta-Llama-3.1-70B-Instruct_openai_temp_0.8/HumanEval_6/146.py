```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function calculates the deepest level of nesting of parentheses for each group in a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses separated by spaces.

    Returns:
    List[int]: A list of integers representing the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # split the input string into groups
    result = []  # initialize a list to store the results

    for group in groups:
        max_depth = 0  # initialize the maximum depth for the current group
        current_depth = 0  # initialize the current depth for the current group

        for char in group:
            if char == '(':  # if the character is an opening parenthesis
                current_depth += 1  # increase the current depth
                max_depth = max(max_depth, current_depth)  # update the maximum depth
            elif char == ')':  # if the character is a closing parenthesis
                current_depth -= 1  # decrease the current depth

        result.append(max_depth)  # append the maximum depth for the current group to the result list

    return result


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of integers representing the deepest level of nesting for each group. The function splits the input string into groups, then iterates over each group to calculate the maximum depth of nesting. The result is a list of integers, where each integer corresponds to the maximum depth of nesting for a group. The script includes a docstring and example usage to demonstrate the function's behavior.