```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # split the input string into groups
    result = []  # initialize a list to store the result

    for group in groups:
        max_depth = 0  # initialize the maximum depth for the current group
        current_depth = 0  # initialize the current depth for the current group

        for char in group:  # iterate over each character in the group
            if char == '(':  # if the character is an opening parenthesis
                current_depth += 1  # increase the current depth
                max_depth = max(max_depth, current_depth)  # update the maximum depth
            elif char == ')':  # if the character is a closing parenthesis
                current_depth -= 1  # decrease the current depth

        result.append(max_depth)  # append the maximum depth for the current group to the result list

    return result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]
```