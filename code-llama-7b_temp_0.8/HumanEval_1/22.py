from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def balance_paren_check(paren_string: str) -> bool:
        """This function checks if a given paren string is balanced.
        >>> balance_paren_check('( ) (( )) (( )( ))')
        True
        >>> balance_paren_check('( () ( ))')
        False
        """
        stack = []
        for char in paren_string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        return not stack

    def get_separate_paren_groups(paren_string: str) -> List[str]:
        """This function returns a list of separate paren groups if the given string is balanced.
        >>> get_separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
        >>> get_separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
        """
        stack = []
        for char in paren_string:
            if char == '(':
                stack.append(char)
            elif char == ')':
                stack.pop()
                if not stack:
                    return stack
        return []

    if balance_paren_check(paren_string) is True:
        return get_separate_paren_groups(paren_string)
    return []

