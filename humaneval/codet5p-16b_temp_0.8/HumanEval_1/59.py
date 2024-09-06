from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if len(paren_string) == 0:
        return []

    if len(paren_string) % 2!= 0:
        return []
    else:
        res = []
        i = 0
        while i < len(paren_string):
            j = i
            count = 1
            while j < len(paren_string):
                if paren_string[j] == '(':
                    count += 1
                elif paren_string[j] == ')':
                    count -= 1
                if count == 0:
                    break
                j += 1
            res.append(paren_string[i:j + 1])
            i = j + 1
        return res

