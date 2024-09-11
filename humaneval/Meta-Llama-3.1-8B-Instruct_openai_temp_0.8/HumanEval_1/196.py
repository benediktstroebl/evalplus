```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string containing multiple groups of nested parentheses, 
    separates those groups into separate strings and returns the list of those.

    The input string can contain multiple groups of balanced parentheses that are not nested within each other.
    Any spaces in the input string are ignored.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a separate group of balanced parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    import re
    # Remove any spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the groups
    groups = []
    
    # Find all substrings in the input string that have balanced parentheses
    for group in re.finditer(r'\([^()]*\)', paren_string):
        # Add the balanced group to the list
        groups.append(group.group())
    
    # Return the list of groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

In this script, we use the `re.finditer` function to find all substrings in the input string that have balanced parentheses. The `r'\([^()]*\)'` regular expression pattern matches any substring that starts with an opening parenthesis, followed by zero or more characters that are not opening or closing parentheses, and ends with a closing parenthesis. The `finditer` function returns an iterator yielding match objects for every non-overlapping occurrence of the pattern in the string. We iterate over these match objects, extract the matched substring (the group of balanced parentheses) using the `group` method, and add it to the `groups` list. Finally, we return the `groups` list.