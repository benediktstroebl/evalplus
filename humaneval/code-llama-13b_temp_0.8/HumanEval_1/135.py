from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # You can solve this question using O(1) space and O(n) time.
    # Use in_group, opened and close_idx to store values needed to separate the groups.
    open_idx = []
    close_idx = []
    opened = 0
    in_group = False
    output = []
    for idx, char in enumerate(paren_string):
        if char == '(':
            opened += 1
            in_group = True
            open_idx.append(idx)
        elif char == ')':
            if in_group:
                opened -= 1
                if opened == 0:
                    in_group = False
                    close_idx.append(idx)
    for open, close in zip(open_idx, close_idx):
        output.append(paren_string[open:close + 1])
    return output

