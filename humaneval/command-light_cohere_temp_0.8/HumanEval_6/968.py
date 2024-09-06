Here's a self-contained Python function that parses and returns the deepest level of nesting in a given string of parentheses:
```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function takes a string of parenthesis groups separated by spaces as input and returns a list of their deepest nesting levels.

    Args:
        string: The input string to parse

    Returns:
    list: The deepest level of nesting in the input string
    """
    # Split the string into lists of parenthesis groups based on spaces
    groups = [list(x) for x in parenthesis_string.split()]
   
    spaces = [''] + groups[1:]
    # Initialize the output list
    output = []
    # Loop through each group of parentheses
    for group in groups:
        # Initialize a counter for the current nesting level
        nesting_level = 0
        # Loop through each character in the group
        for i, char in enumerate(group):
            if char == '(':
                # If the character is an open parenthesis, increment the nesting level
                nesting_level += 1
            elif char == ')':
                # If the character is a closed parenthesis, reset the nesting level
                nesting_level -= 1
        # If the nesting level reaches 0, add this level to the output list
        if nesting_level == 0:
            output.append(nesting_level)
    return output
```
This function takes a string of parenthesis groups separated by spaces as input and returns a list of their deepest nesting levels. The function then splits the string into lists of parenthesis groups based on spaces and then loops through each group, keeping track of the current nesting level. The function adds the levels to the output list when the nesting level reaches 0.