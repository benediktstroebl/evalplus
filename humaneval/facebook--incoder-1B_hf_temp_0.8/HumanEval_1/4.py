from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parens_groups = []
    parens_stack = []
    parens_depth = 0
    parens_string = str(paren_string).strip()
    for paren in parens_string:
        if paren == ')':
            if parens_depth!= 0:
                parens_stack.append(parens_string)
                parens_depth = 0
        elif paren == ']':
            if parens_depth > 0:
                parens_stack.pop()
                parens_depth -= 1
            else:
                parens_groups.append("".join(parens_stack))
                parens_stack = []
                parens_depth = 0
        else:
            parens_depth += 1
            if paren == ')':
                parens_depth += 1
                if parens_depth > 0:
                    parens_stack.append(parens_string)
                    parens_depth = 0
            else:
                parens_stack.append(parens_string)

    if parens_stack:
        parens_groups.append("".join(parens_stack))

    return parens_groups

