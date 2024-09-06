from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    opening_parens = []
    closing_parens = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            opening_parens.append(i)
        elif paren_string[i] == ")":
            closing_parens.append(i)
            # if that is the last char, it is no longer balanced
            if i == len(paren_string) - 1:
                break
            elif opening_parens and closing_parens:
                if closing_parens[-1] < opening_parens[-1]:
                    result.append(paren_string[opening_parens[-1] + 1:closing_parens[-1]])
                    opening_parens.pop()
                    closing_parens.pop()
                else:
                    result.append(paren_string[opening_parens[-1] + 1:-1])
                    opening_parens.pop()
                    closing_parens.pop()
        i += 1
    return result

