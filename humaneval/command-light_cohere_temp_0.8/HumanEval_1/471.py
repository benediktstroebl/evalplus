```python
from typing import List
def separate_paren_groups(parenthesis_string: str) -> List[str]:
    """Separate parentheses into a list of groups.
    Return a list of strings where each string represents a group of open-ended parentheses properly balanced.
    """ The balanced groups of open and closed parentheses
    """
    # split the string into list of character groups
    groups = [char for char in parenthesis_string if char == '('] + [char for char in parenthesis_string if char == ')']
    
    # remove any spaces in the string
    cleaned_groups = [char for char in groups if char != ' ')
    
    return cleaned_groups
```