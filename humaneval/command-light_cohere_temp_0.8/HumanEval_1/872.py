```python
from typing import List

def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Function that takes a list of strings as input and returns a list of properly formatted strings with separated groups of parentheses.
    """
    Function takes a list of strings and loops through each string in the list. The string is split into a list of substrings based on spaces. Then, it takes each substring as a new string and returns the list of strings.
    """ Return an example of the function:
    >>> separate_paren_groups([])
    []
    >>> separate_paren_groups('( )(( )) )')
    ['()', '()()']
    >>> separate_paren_groups('( ) )( (( ) )')')
    ['()', '()()', '(')']
    >>> separate_paren_groups('( )( ( ) )( )')
    ['()()', '(')']
    """
    # Split the string into substrings based on spaces
    substrings = [sub for sub in parentheses]

    # Flatten the list of substrings into strings
    flattened_strings = ' '.join(substrings)

    return [flattened_strings]
```