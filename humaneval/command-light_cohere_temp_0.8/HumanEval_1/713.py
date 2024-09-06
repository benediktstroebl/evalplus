```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    This function takes a string of parenthesis groups as input and returns a list of separate parenthesis strings.
    It are designed to handle any number of groups and any content within the parentheses.
    """
    balanced parentheses are defined as having only one opening and closing parenthesis in a row.
    Return: a list of strings where each string represents a balanced parenthesis group.
    """
penults are also removed.
    """

Example usage:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Split parenthesis into individual strings
    parents = [p for p in parentheses if p == '('] + [p for p in parentheses if p == ')']
    # Return list of strings
    return parents
```