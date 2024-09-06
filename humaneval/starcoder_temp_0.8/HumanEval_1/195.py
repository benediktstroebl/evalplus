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
    elif len(paren_string) == 1:
        return [paren_string]
    elif paren_string[0] == ")":
        return [paren_string]
    else:
        index = paren_string.find(")")
        left = separate_paren_groups(paren_string[1:index])
        right = separate_paren_groups(paren_string[index + 2 :])
        if left:
            result = []
            for item in left:
                result.append("(" + item)
            if right:
                for item in right:
                    result.append(")" + item)
            return result
        else:
            return right

