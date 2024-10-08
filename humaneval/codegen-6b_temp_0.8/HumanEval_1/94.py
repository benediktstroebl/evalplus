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
    output = []
    for i in range(len(paren_string)):
        ch = paren_string[i]
        if ch == ')':
            curr = paren_stack.pop()
            while curr != '(':
                output.append(curr)
                curr = paren_stack.pop()
        elif ch == '(':
            paren_stack.append(ch)
        elif ch == ' ':
            continue
        else:
            output.append(ch)

    if paren_stack:
        raise Exception('Not cleared stack')
    return output

