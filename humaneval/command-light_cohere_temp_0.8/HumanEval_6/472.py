Here's the self-contained Python script that solves the markdown code block problem:
```python
from typing import List
def parse_nested_parens(parenthesis_string: str) -> List[int]:
    """
    This function is designed to parse through a string of nested parentheses. 
    It returns a deep levels of nesting for every group of parentheses.
    Args: 
        - String of parenthesis with groups separated by spaces. 
    Returns: A list of deepest level of nesting for each group of parentheses.
    """
    number of parentheses at each level
    """
    # Initialize empty list to store the output
    output = []
    # Define a function to find the deepest level of nesting for a group of parentheses
    def find_deeper_nesting(group_string: str) -> int:
        # Initialize empty stack of numbers
        stack = []
        # Define the characters in the group string to be numbers from 0 to 9
        group_chars = [char for char in group_string if char.isdigit()]
        number = int('0' in group_chars)
        # Loop to find the highest value in the group string
        for char in group_chars:
            # Add the current char to the stack
            stack.append(int(char))
        # Return the highest value in the stack, which is the deepest level of nesting
        return max(stack)
    # Loop to parse each group of parentheses in the parenthesis string
    for group in parenthesis_string.split('(' ')):
        # Add the deepest level of nesting found for this group to the output
        output.append(find_deeper_nesting(group))
    return output
```
The provided code uses a function `parse_nested_parens` to parse and return the deepest level of nesting for each group of parentheses in a given string. The `find_deeper_nesting` function utilizes a stack data structure to keep track of the deepest level of nesting for each group. The function then iterates through the string, and at each iteration adds the current character's value to the stack. The maximum value in the stack at the end is the deepest level of nesting, which is then added to the output list.