from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    result = []
    # The first open paren will be added to the stack
    for char in paren_string:
        if char == "(":
            stack.append("(")
        # If we have more close parens than open parens, we need to add an empty string to the result
        elif char == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                result.append("")
        # If we have no open parens, we should add the current chars to the result
        if len(stack) == 0:
            result.append("")
        # This is a close paren, so we should add it to the result
        if char == ")":
            result[-1] += char
    # Convert the list of strings into a list of lists
    output_list = [list(x) for x in result]
    return output_list

