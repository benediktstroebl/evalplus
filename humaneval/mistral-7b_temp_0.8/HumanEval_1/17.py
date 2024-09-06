from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # if paren_string == "":
    #     return []

    # # if not has_unbalanced_parentheses(paren_string):
    # #     return [paren_string]

    # # return []

    # # #
    # # #

    # def has_unbalanced_parentheses(paren_string: str):
    #     """ Returns True if the input string has unbalanced parentheses.
    #     Otherwise, return False.
    #     >>> has_unbalanced_parentheses('()')
    #     False
    #     >>> has_unbalanced_parentheses('( )')
    #     False
    #     >>> has_unbalanced_parentheses('( ( ))')
    #     False
    #     >>> has_unbalanced_parentheses('( ( ) )')
    #     True
    #     >>> has_unbalanced_parentheses('( )( )')
    #     False
    #     >>> has_unbalanced_parentheses(')(')
    #    
