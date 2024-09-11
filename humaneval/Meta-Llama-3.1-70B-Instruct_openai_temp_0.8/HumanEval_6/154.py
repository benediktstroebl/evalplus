```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list of the deepest level of nesting for each group.

    :param paren_string: A string of multiple groups of nested parentheses separated by spaces.
    :return: A list of the deepest level of nesting for each group.
    """
    groups = paren_string.split()  # Split the input string into groups
    result = []  # Initialize an empty list to store the results

    for group in groups:
        max_level = 0  # Initialize the maximum level for the current group
        current_level = 0  # Initialize the current level for the current group

        for char in group:
            if char == '(':  # If the character is an opening parenthesis
                current_level += 1  # Increase the current level
                max_level = max(max_level, current_level)  # Update the maximum level
            elif char == ')':  # If the character is a closing parenthesis
                current_level -= 1  # Decrease the current level

        result.append(max_level)  # Append the maximum level for the current group to the result

    return result


# Example usage:
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```