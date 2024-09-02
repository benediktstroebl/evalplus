from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # the algorithm is to iterate through the string and add each character to a separate list. When we find
    # an open brace, add an empty string to the list. When we find a closed brace, pop from the end until we
    # find the corresponding opening brace. If we have any parentheses after the opening brace, add them
    # to the list.

    if not paren_string:
        return []
    output_list: List[str] = []
    current_paren_string: List[str] = []
    open_braces: int = 0
    close_braces: int = 0
    for char in paren_string:
        if char == '(':
            open_braces += 1
            output_list.append('')
        elif char == ')':
            close_braces += 1
        current_paren_string.append(char)
        if open_braces == close_braces and open_braces > 0:
            pop_list: List[str] = []
            for _ in range(open_braces):
                pop_list.append(current_paren_string.pop())
            output_list[-1] += "".join(pop_list)[1:-1]
            open_braces = 0
            close_braces = 0
    return output_list

