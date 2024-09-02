from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parentheses_stack = []
    result = []
    current_string = ""

    for i, char in enumerate(paren_string):
        if char == "(":
            parentheses_stack.append(i)
        elif char == ")":
            parentheses_stack.pop()
            if parentheses_stack:
                # update the result
                result.append(current_string[len(current_string)-parentheses_stack[0]:])
                # update the current_string
                current_string = current_string[parentheses_stack[0]:]
            else:
                # add the last part of the string
                result.append(current_string)
        else:
            current_string += char

    # add the last part of the string
    result.append(current_string)
    return result

