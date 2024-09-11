```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.

    :param paren_string: A string of groups separated by spaces, each group containing nested parentheses.
    :return: A list of integers representing the deepest level of nesting of parentheses in each group.
    """
    result = []  # Initialize a list to store the result
    for group in paren_string.split():  # Split the input string into groups
        level = 0  # Initialize the level of nesting for the current group
        max_level = 0  # Initialize the maximum level of nesting for the current group
        for char in group:  # Iterate over each character in the group
            if char == '(':  # If the character is an opening parenthesis
                level += 1  # Increase the level of nesting
                max_level = max(max_level, level)  # Update the maximum level of nesting
            elif char == ')':  # If the character is a closing parenthesis
                level -= 1  # Decrease the level of nesting
                if level < 0:  # If the level of nesting becomes negative
                    level = 0  # Reset the level of nesting
        result.append(max_level)  # Append the maximum level of nesting for the current group to the result
    return result  # Return the result

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))  # Output: [2, 3, 1, 3]
```

This script defines a function `parse_nested_parens` that takes a string of groups as input and returns a list of integers representing the deepest level of nesting of parentheses in each group. The function iterates over each character in each group, updating the level of nesting and the maximum level of nesting as it encounters opening and closing parentheses. Finally, it appends the maximum level of nesting for each group to the result list and returns the list.