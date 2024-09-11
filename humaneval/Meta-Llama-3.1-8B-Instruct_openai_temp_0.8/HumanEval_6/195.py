```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of multiple groups of nested parentheses separated by spaces.
    It returns a list where each element is the maximum level of nesting of the corresponding group.

    Args:
        paren_string (str): A string of multiple groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list where each element is the maximum level of nesting of the corresponding group.
    """
    groups = paren_string.split()
    result = []

    for group in groups:
        # Initialize level and max_level
        level = 0
        max_level = 0

        # Iterate through each character in the group
        for char in group:
            # If the character is an opening parenthesis, increase level
            if char == '(':
                level += 1
                max_level = max(max_level, level)
            # If the character is a closing parenthesis, decrease level
            elif char == ')':
                level -= 1

        # Add the max_level to the result list
        result.append(max_level)

    return result


# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script works by splitting the input string into groups, then iterating through each group to calculate the maximum level of nesting. It uses a level variable to keep track of the current level of nesting, and a max_level variable to keep track of the maximum level encountered so far. If it encounters an opening parenthesis, it increments level and max_level. If it encounters a closing parenthesis, it decrements level. Finally, it adds max_level to the result list.