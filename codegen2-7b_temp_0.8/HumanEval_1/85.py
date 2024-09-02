from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output = []
    paren_stack = []
    current_paren = ""
    for char in paren_string:
        if char == "(":
            current_paren += "("
            paren_stack.append(current_paren)
            current_paren = ""
        elif char == ")":
            if current_paren == "":
                raise ValueError(f"No open parenthesis at {paren_string}")
            current_paren = paren_stack.pop() + ")"
            output.append(current_paren)
            current_paren = ""

    return
