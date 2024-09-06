from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    groups = []
    curr_group = []
    for i in range(len(paren_string)):
        curr_char = paren_string[i]
        if curr_char == '(' or curr_char == ')':
            if curr_group == []:
                curr_group.append(curr_char)
            else:
                curr_group.append(curr_char)
                if curr_char == ')' and curr_group[-1] == '(':
                    groups.append(''.join(curr_group))
                    curr_group = []
    return groups

