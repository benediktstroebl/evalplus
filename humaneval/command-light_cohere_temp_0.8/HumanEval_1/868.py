```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Separate groups of parentheses into individual strings and return them as a list.
    Input is a list of strings containing multiple groups of parentheses.
    Returns a balance each open brace properly and not nested within each other
    """
    output = []
    for parantheses in parentheses:
        # skip spaces
        parantheses = parantheses.replace(' ', '')
        
        # find all closed parentheses
        closing_parents = [parent for parent in '([{])' if parent.isspace()]
        
        # split the open and close parentheses
        output.append(''.join(closing_parents) + parantheses)
    return output
``` 
This function takes a list of strings (parentheses) as input and returns a list of strings. It processes the list, removes spaces, finds all closing parentheses, and then opens and closes the parentheses to create individual strings.