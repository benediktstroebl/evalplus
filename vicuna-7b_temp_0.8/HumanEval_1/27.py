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
    output = []
    for opening, closing in [(',', ')'], (')', ']']}:
        for i, char in enumerate(paren_string):
            if char == opening:
                stack.append(i)
                if not stack or stack[-1] != opening:
                    raise ValueError('Opening brace not properly closed')
            elif char == closing:
                output.append(paren_string[stack[-1]:i])
                stack.pop()
                if not stack:
                    raise ValueError('Closing brace not properly matched')
        else:
            output.append(paren_string[i:])
    return output
