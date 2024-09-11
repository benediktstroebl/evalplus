```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of integers representing the deepest level of nesting for each group of parentheses.
    """
    groups = paren_string.split()  # split the input string into groups
    result = []  # initialize an empty list to store the results

    for group in groups:
        max_depth = 0  # initialize the maximum depth for the current group
        current_depth = 0  # initialize the current depth for the current group

        for char in group:
            if char == '(':  # if the character is an opening parenthesis
                current_depth += 1  # increment the current depth
                max_depth = max(max_depth, current_depth)  # update the maximum depth if necessary
            elif char == ')':  # if the character is a closing parenthesis
                current_depth -= 1  # decrement the current depth

        result.append(max_depth)  # append the maximum depth for the current group to the result list

    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```