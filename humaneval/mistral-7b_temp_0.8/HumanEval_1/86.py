from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def is_balanced(s: str) -> bool:
        """ Check if the given string is balanced, i.e., the number of opening parentheses is equal to the number
        of closing parentheses. """
        counter = 0
        for char in s:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1

        return counter == 0

    def get_balanced_group(s: str) -> str:
        """ Get the next group of balanced parentheses from the given string. If the given string does not contain
        any balanced group, return the empty string. """
        index = 0
        while index < len(s):
            index = s.find('(', index)
            if index == -1:
                break
            index = s.find(')', index+1)
            if index == -1:
                break
            if index+1 >= len(s) or s[index+1] != '(':
                break
            if index < 0 or index > len
