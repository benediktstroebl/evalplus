```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Function to separate groups of parentheses into separate strings
    
    Input: string containing multiple groups of nested parentheses
    Output: list of separated strings
    """
    # Split the string into a list of lines based on newlines
    lst = parenstring.splitlines()
    
    # Separate the Won't work without this split, and this way is certainly valid for any string with any number of newlines
    # Remove extra spaces from each line
    lst = [line.replace(''.join(c.strip(' ') for c in line) for line in lst)
    
    # Use list of strings to split into individual groups of parentheses
    groups = [list(x.split()) for x in lst]
    
    # Sort the list of strings by length, with the shortest length first
    sorted_groups = sorted(groups, key=len, reverse=True)
    
    # Return the list of separated strings
    return [p for p in sorted_groups]
``` 
This code follows the problem statement, which is to separate parentheses into separate strings. It achieves this by splitting the strings based on newlines, removing extra spaces, and then using list of strings to split into individual groups. Finally, it returns the list of separated strings.