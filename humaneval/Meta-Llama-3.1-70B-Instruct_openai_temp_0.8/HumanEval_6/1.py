```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of integers, where each integer represents the deepest level of nesting of parentheses in the corresponding group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of integers representing the deepest level of nesting of parentheses in each group.
    """
    groups = paren_string.split()  # Split the input string into groups of parentheses
    result = []  # Initialize an empty list to store the results

    for group in groups:
        max_depth = 0  # Initialize the maximum depth for the current group
        current_depth = 0  # Initialize the current depth for the current group

        for char in group:
            if char == '(':  # If the character is an opening parenthesis, increment the current depth
                current_depth += 1
                max_depth = max(max_depth, current_depth)  # Update the maximum depth
            elif char == ')':  # If the character is a closing parenthesis, decrement the current depth
                current_depth -= 1

        result.append(max_depth)  # Append the maximum depth for the current group to the result list

    return result  # Return the result list


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```