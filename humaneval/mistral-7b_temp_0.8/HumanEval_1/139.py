from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    opening_paren = '('
    closing_paren = ')'

    # returns index of opening paren, or -1 if it is not present
    def find_index(paren: str) -> int:
        return paren_string.find(paren)

    # return index of closing paren, or -1 if it is not present
    def find_closing_index(paren: str) -> int:
        return paren_string.rfind(paren)

    # stack of parens that are currently open
    stack = []

    # index of next open paren
    open_idx = find_index(opening_paren)

    # index of next closing paren
    close_idx = find_closing_index(closing_paren)

    while close_idx != -1 or open_idx != -1:
        # check if we have a balanced pair
        if close_idx != -1 and close_idx < open_idx:
            # close the pair and add to the list
            stack.append(paren_string[open_idx:close_idx+1])
