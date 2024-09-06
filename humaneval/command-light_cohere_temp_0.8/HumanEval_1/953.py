```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    This function takes a string of parenthesis groups as input and returns a list of separate strings.

    It uses an innovative approach of ignoring spaces and creating a stack of open parenthesis to efficiently separate the groups.
    Returns: list of strings, each one representing a group of open parenthesis.

    """
    uses Python's built-in function 'reversed' to get all the open parenthesis in the string.
    """ Separates groups into the strings until all the closed parenthesis is reached, then the stack is empty. The function returns a list containing the strings of the groups of closed parenthesis.
    """ The open parenthesis is crucial to make sure that the groups are correctly separated. 
"""

    Test Cases
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    >>> separate_paren_groups('( ) (( ) ) (( ))')
    ['()', '((())')', '(()())']
    """

I hope this code can effectively solve the problem of separating parentheses and passes all the test cases.