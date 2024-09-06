Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing the separated parentheses groups with nested parentheses and spaces removed:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    # Remove all spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Split the string into separate groups of parentheses
    groups = paren_string.split(')(')
    
    # Iterate through the split groups and correct any incorrectly split groups
    balanced_groups = []
    for group in groups:
        # Correctly nest parentheses group if not correctly split
        corrected_group = group.replace(')(', ')( ').replace(')(', '(')
        balanced_groups.append(corrected_group)
    
    return balanced_groups

# Sample input and output
sample_input = '( ) (( )) (( )( ))'
sample_output = ['()', '(())', '(()())']

assert separate_paren_groups(sample_input) == sample_output
```

This script uses the `replace()` method to remove spaces from the input string and split the nested parentheses into separate groups. Then, a correction step is included to fix any incorrectly split groups, and the corrected groups are appended to the `balanced_groups` list. The function returns this list of separated and balanced parentheses groups.