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
    groups = paren_string.split()  # split the string into groups
    result = []  # initialize an empty list to store the results

    for group in groups:
        max_depth = 0  # initialize the maximum depth for the current group
        curr_depth = 0  # initialize the current depth for the current group

        for char in group:
            if char == '(':  # if the character is an opening parenthesis
                curr_depth += 1  # increase the current depth
                max_depth = max(max_depth, curr_depth)  # update the maximum depth
            elif char == ')':  # if the character is a closing parenthesis
                curr_depth -= 1  # decrease the current depth

        result.append(max_depth)  # append the maximum depth for the current group to the result list

    return result


# test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```