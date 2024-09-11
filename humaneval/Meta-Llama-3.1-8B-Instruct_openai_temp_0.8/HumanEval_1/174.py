```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into a list of separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a group of nested parentheses.
    """
    
    group_list = []
    temp_group = ''
    
    for char in paren_string:
        if char == '(':
            temp_group += char
        elif char == ')':
            if temp_group:  # Check if temp_group is not empty
                group_list.append(temp_group + char)
                temp_group = ''
            else:
                temp_group += char  # If temp_group is empty, ignore the ')'
    
    return group_list

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings, each containing a separate group of parentheses. The function uses a temporary string `temp_group` to build up each group as it iterates through the input string. When it encounters a closing parenthesis, it adds the current group to the list and resets the temporary string. If it encounters a closing parenthesis when the temporary string is empty, it ignores it. Finally, it returns the list of groups. The test case at the end of the script demonstrates its usage.