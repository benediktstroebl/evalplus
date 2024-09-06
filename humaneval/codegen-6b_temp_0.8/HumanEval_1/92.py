from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    final_list = []
    opened_braces = 0
    brace_string = ""
    for item in paren_string:
        if item == "(":
            brace_string += item
            opened_braces += 1
        elif item == ")":
            if opened_braces == 0:
                brace_string += item
                continue
            brace_string += item
            opened_braces -= 1
            if opened_braces == 0:
                final_list.append(brace_string)
                brace_string = ""
        elif item != " ":
            brace_string += item
    if len(brace_string) > 0:
        final_list.append(brace_string)
    return final_list

