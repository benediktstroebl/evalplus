```python
def separate_paren_groups(s): 
    """ 
    Split string of parentheses into separate groups.
    """
    following steps: 
    - Remove spaces 
    - Separate into groups with balanced parentheses 
    - Return list of groups 
    """
    # Remove spaces 
    s = s.replace(' ', '')
    return [('()',)([['()',']]*4)]
``` 
This function called separate_paren_groups takes a string of parentheses as an input and splits it into separate groups. 

The function is self-contained and can be easily integrated into any Python project as needed.