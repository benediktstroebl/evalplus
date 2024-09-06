from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    """BEGIN PSEUDOCODE"""
    # s = list(paren_string)
    # i = 0
    # while i < len(s):
    #   if s[i] == '(':
    #     left_paren_index = i
    #     open_parens = 1
    #     i += 1
    #     while open_parens != 0:
    #       if s[i] == '(':
    #         open_parens += 1
    #         i += 1
    #       elif s[i] == ')':
    #         open_parens -= 1
    #         i += 1
    #     right_paren_index = i - 1
    #     s[left_paren_index:right_paren_index] = [s[left_paren_index:right_paren_index]]
    # return s
    """ END PSEUDOCODE"""
    s = list(paren_string)
    i = 0
    paren_groups = []
    while i < len(s):
        if s[i] == '(':
            left_paren_index = i
            open_parens = 1
            i += 1
            while open_parens != 0:
                if s[i] == '(':
                    open_parens += 1
                    i += 1
                elif s[i] == ')':
                    open_parens -= 1
                    i += 1
            right_paren_index = i - 1
            paren_groups.append(s[left_paren_index:right_paren_index])
            s[left_paren_index:right_paren_index] = []
    return paren_groups

