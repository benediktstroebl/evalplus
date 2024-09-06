from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    current_paren = 0
    output = []
    while current_paren < len(paren_string):
        if paren_string[current_paren] == "(":
            paren_stack.append(paren_string[current_paren])
            output.append(paren_string[current_paren])
        else:
            if len(paren_stack) > 0 and paren_stack[-1] == "(":
                paren_stack.pop()
                output.append(paren_string[current_paren])
            else:
                while len(paren_stack) > 0 and paren_stack[-1] != "(":
                    output.append(paren_string[current_paren])
                    current_paren += 1
    return output

