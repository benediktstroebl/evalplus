from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []

    def _separate_paren_groups(paren_groups, paren_groups_left, index):
        """ Creates new groups from the current group string, that is,
        groups that are either separated by a space or are the end of the string
        side by side with another group.
        """
        if index == len(paren_string):
            paren_groups.append(''.join(paren_groups))
        elif paren_string[index] == ' ':
            _separate_paren_groups(paren_groups, paren_groups_left, index + 1)
            paren_groups[paren_groups_left].append(' ')
        elif paren_string[index] == ')':
            _separate_paren_groups(paren_groups, paren_groups_left + 1, index + 1)
            paren_groups[paren_groups_left].append(')')
        else:
            _separate_paren_groups(paren_groups, paren_groups_left, index + 1)
            paren_groups[paren_groups_left].append(paren_string[index])

    _separate_paren_groups(paren_groups, 0, 0)
    return paren_groups

