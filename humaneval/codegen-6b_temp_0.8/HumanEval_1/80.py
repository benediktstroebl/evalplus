from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    nested_braces = []
    result = []

    i = 0
    j = 0

    while i < len(paren_string):
        char = paren_string[i]
        if char == "(":
            j = i + 1
            nested_braces.append([j, char])
            i = j
        elif char == ")":
            if len(nested_braces) == 0:
                result.append(paren_string[i + 1:])
                break
            else:
                last_brace = nested_braces.pop()
                if last_brace[0] == i:
                    result.append(paren_string[last_brace[0] + 1: i])
                    i = last_brace[0]
                else:
                    result.append(paren_string[last_brace[0] + 1: last_brace[0]])
                    i = last_brace[0]
        elif char == " ":
            i += 1
        else:
            i += 1

    if len(nested_braces) == 0:
        return [paren_string]
    else:
        return result

