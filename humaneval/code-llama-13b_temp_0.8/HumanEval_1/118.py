from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # solution with stacks
    paren_stack = []
    paren_strings = []
    current_string = ""
    for paren in paren_string:
        if paren != " ":
            current_string += paren
            if paren == "(":
                paren_stack.append(paren)
            elif paren == ")":
                paren_stack.pop()
                if len(paren_stack) == 0:
                    paren_strings.append(current_string)
                    current_string = ""
    return paren_strings

    # solution with regular expressions
    # import re
    # return re.findall(r'\([^()]*\)', paren_string)

