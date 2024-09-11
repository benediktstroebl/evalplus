```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers, where each integer represents the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers, where each integer represents the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # Split the input string into groups
    result = []  # Initialize an empty list to store the results

    for group in groups:
        max_depth = 0  # Initialize the maximum depth for the current group
        current_depth = 0  # Initialize the current depth for the current group

        for char in group:
            if char == '(':  # If the character is an opening parenthesis, increase the current depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis, decrease the current depth
                current_depth -= 1

        result.append(max_depth)  # Append the maximum depth for the current group to the result list

    return result


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```
This script defines a function `parse_nested_parens` that takes a string of multiple groups of nested parentheses separated by spaces and returns a list of integers, where each integer represents the deepest level of nesting for each group. The function splits the input string into groups, then iterates over each group to calculate the maximum depth of nesting. The result is a list of integers, where each integer represents the deepest level of nesting for each group.