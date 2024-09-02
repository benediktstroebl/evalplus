from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def find_matching_paren(open_paren_index, paren_string):
        for i in range(open_paren_index+1, len(paren_string)):
            if paren_string[i] == '(':
                continue
            else:
                return i

    def find_groups(paren_string):
        open_paren_index = paren_string.find('(')
        if open_paren_index == -1:
            return []
        else:
            matching_close_paren = find_matching_paren(open_paren_index, paren_string)
            return find_groups(paren_string[matching_close_paren+1:]) + [paren_string[open_paren_index:matching_close_paren+1]]

    return find_groups(paren_string)

