```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separates groups of parentheses into individual strings.

    :
    Input is a string of potential parenthesis groups.
    Returns a String list where each group of parentheses is separated into an individual string.
    """
    list comprehension and space expansion: ['()', '((()))', '(()())']
    """
    return [ parentheses for parentheses in s if parentheses != '(' and parentheses != ')']
``` 
The function 'separate_paren_groups' takes an input string 's' and returns a list of strings created from individual groups of parentheses in the input. It utilizes list comprehension to iterate over each non-parenthesis character '(' or ')') and create a new string with balanced parentheses. The string is split into a list of balanced parentheses.