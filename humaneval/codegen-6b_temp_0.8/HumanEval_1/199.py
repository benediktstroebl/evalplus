from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []
    paren_stack = []
    current_string = ""
    new_string = ""
    result = []
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            paren_stack.append(paren_string[i])
            current_string += paren_string[i]
        elif paren_string[i] == ")" and len(paren_stack) == 0:
            raise ValueError(f"Unmatched close paren: {paren_string[i]}")
        elif paren_string[i] == ")" and len(paren_stack) > 0:
            paren_stack.pop()
            current_string += paren_string[i]
        else:
            current_string += paren_string[i]
        if len(current_string) == 2:
            new_string = new_string[1:-1]
            result.append(new_string)
            new_string = ""
            current_string = ""
    if len(current_string) > 0:
        new_string = new_string[1:-1]
        result.append(new_string)
    return result

