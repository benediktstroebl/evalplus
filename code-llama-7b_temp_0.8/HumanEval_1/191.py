from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # 1. Find all the groups of nested parentheses.
    # 2. Separate each group into its own string.
    # 3. Return the list of those strings.
    open_parens = 0
    results = []
    curr_string = ""
    for paren in paren_string:
        if paren == "(":
            if open_parens == 0:
                curr_string += paren
            open_parens += 1
        elif paren == ")":
            open_parens -= 1
            if open_parens == 0:
                results.append(curr_string)
                curr_string = ""
            else:
                curr_string += paren
        else:
            curr_string += paren
    return results

