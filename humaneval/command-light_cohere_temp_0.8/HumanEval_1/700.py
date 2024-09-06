```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """ Function to separate and return groups of parentheses.
    Input is a list of strings containing parentheses. Function will return a for each string, separate and return groups of parentheses with balanced open and close parentheses.
    Args: 
    - List of strings containing parentheses 
    Returns: List of separated strings containing only parentheses
    """
    # Initialize empty list to store results
    output = []
    
    # Iterate through each string in the input list
    for string in parentheses:
        # Use string slicing to remove non-parentheses characters and split into list of char
        char_list = string[1:-1]  # Remove the first and last character (which are both parentheses)
        # Use list comprehension to separate each group of parentheses
        groups = [char for char in char_list if char == char.))))
       
       
       
        then, continue to next iteration
        output.add(groups)
        
    return output
```