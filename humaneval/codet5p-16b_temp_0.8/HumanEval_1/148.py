from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    ans = []
    open_count = 0
    is_opened = False
    temp = []
    for char in paren_string:
        if char == '(':
            open_count += 1
            is_opened = True
        elif char == ')':
            open_count -= 1
            if is_opened:
                ans.append(''.join(temp))
                temp = []
                is_opened = False
            else:
                temp.append(char)
    ans.append(''.join(temp))
    return ans

