```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Function to separate parenthesis groups into individual strings
    Returns: list of separated strings
    """
    # Create an empty list to store the separated strings
    separated_strings = []
    
    # Loop through each group of parentheses
    for group in parentheses:
        # Remove the leading and trailing whitespaces around each group
        group = group.center
       
        spaces = ' '.join(filter(x -> x!isspace(), x != ' '))
        
        # Remove nested parentheses within each group
        group = ''.join(x for x in group if x != '(' and x != ')')
        
        # Append the current group to the list
        separated_strings.append(group)
    
    return separated_strings
``` 
This script defines a function called `separate_paren_groups` that takes a string of parenthesis groups as an input and returns a list of separated strings, which are the individual groups of parentheses. The function uses a `join spaces` to keep the groups together and separate them from any nested parentheses.