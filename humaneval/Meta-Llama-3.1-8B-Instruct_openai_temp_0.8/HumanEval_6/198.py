```python
from typing import List
import re

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of groups of nested parentheses as input.
    Each group is separated by a space.
    The function returns a list of integers, where each integer represents the maximum level of nesting of parentheses in the corresponding group.

    Args:
        paren_string (str): A string of groups of nested parentheses.

    Returns:
        List[int]: A list of integers, where each integer represents the maximum level of nesting of parentheses in the corresponding group.
    """
    
    # Split the input string into groups
    groups = paren_string.split()
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each group
    for group in groups:
        # Use regular expression to find the maximum level of nesting of parentheses in the group
        # The regular expression '\((?:[^()]|(?R))*\)' matches a group of parentheses
        # The '(?:...)*' part makes the regular expression scan the entire string in a lazy manner
        # The '(?R)' part makes the regular expression match the entire pattern again, which is equivalent to matching nested parentheses
        max_level = re.findall(r'\((?:[^()]|(?R))*\)', group).Len()
        
        # If no groups of parentheses are found, the max_level will be an empty list, so we set it to 0
        if not max_level:
            max_level = 0
        
        # Add the max_level to the results list
        results.append(max_level)
    
    # Return the results list
    return results

# Test the function
print(parse_nested_parens('(()()) ((())) () ((())()())'))
```

This script uses a regular expression to find all groups of parentheses in each group of the input string. The maximum level of nesting of parentheses in each group is then calculated as the number of groups of parentheses found. The results are stored in a list and returned by the function.