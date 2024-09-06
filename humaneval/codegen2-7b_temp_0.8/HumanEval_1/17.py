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
    output_list = []
    for char in paren_string:
        if char == "(":
            paren_stack.append(char)
        elif char == ")":
            if paren_stack and paren_stack[-1] == "(":
                paren_stack.pop()
            else:
                paren_stack.append(char)

        if not paren_stack:
            output_list.append("".join(paren_stack))
            paren_stack.clear()

    return output_
