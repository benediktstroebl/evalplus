from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def split_by_depth(paren_string: str, curr_depth: int) -> List[str]:
        if curr_depth == 0:
            return [paren_string]
        if paren_string.find(')') == -1:
            return []
        if paren_string.find(')') < paren_string.find('('):
            return split_by_depth(paren_string[paren_string.find(')') + 1:], curr_depth - 1)
        else:
            return [paren_string[:paren_string.find(')') + 1]] + split_by_depth(paren_string[paren_string.find(')') + 1:], curr_depth)

    return list(filter(lambda x: x, split_by_depth(paren_string, paren_string.count('('))))
