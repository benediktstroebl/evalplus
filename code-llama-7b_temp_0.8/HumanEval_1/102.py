from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return_val = []
    current_string = ""
    paren_stack = []
    for char in paren_string:
        if char in ("(", "["):
            paren_stack.append(char)
        elif char == ")":
            if len(paren_stack) == 0:
                return None
            paren = paren_stack.pop()
            if paren != "(":
                return None
        elif char == "]":
            if len(paren_stack) == 0:
                return None
            paren = paren_stack.pop()
            if paren != "[":
                return None
        if char in (")", "]"):
            current_string += char
            if len(paren_stack) == 0:
                return_val.append(current_string)
                current_string = ""
        else:
            current_string += char
    return return_val

