```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """ Separate groups of parentheses into separate strings.

    : We string containing multiple groups of nested parentheses.
   : Return list of strings, each containing a group of parentheses.
    """
    string = '} ) ( () () () )'
    #Split the string into individual characters
    characters = s.split()
    string
    separated by spaces
    #Group the characters by open and close parentheses
    groups = [char for char in characters if char == '(' or char == ')']
    # Remove any extra spaces between groups
    spaces = [''] * len(groups)
    groups = [group.join(' ') for group in groups] + spaces
    return groups
```