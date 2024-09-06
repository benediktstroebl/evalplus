```python
from typing import List

def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    This function takes a list of strings, each representing a group of parentheses.
    Each string is checked for valid parenthesis groups, and the valid ones are returned as a list.
    >>> separate_paren_groups([ '()', '( )', '(() )', '( )()', '()()'])
    ['()', '(())', '(()())']
    """
    # Initialize empty list to store the valid parenthesis groups
    results = []
    
    # Iterate through the list of strings
    for current_str in parentheses:
        # Use string slicing to find the next open parenthesis
        next_open_pos = current_str.find('(', None)
        next_open_pos, ')' in current_str)
        if next_open_pos is not None:
            # If found, it means this is a valid group of parentheses
            # Add the group to the results list
            results.append(current_str[next_open_pos:])
    
    return results
```