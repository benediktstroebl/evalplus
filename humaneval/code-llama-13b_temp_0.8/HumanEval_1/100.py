from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    nested = False
    start = 0
    end = len(paren_string) - 1
    paren_list: List[str] = []

    while start < end:
        if paren_string[start] == "(":
            if not nested:
                nested = True
                start += 1
                continue
            if nested:
                while paren_string[end] != ")":
                    end -= 1
                paren_list.append(paren_string[start : end + 1])
                nested = False
                start = end + 1
                end = len(paren_string) - 1
                continue
        start += 1
        end -= 1

    return paren_list

