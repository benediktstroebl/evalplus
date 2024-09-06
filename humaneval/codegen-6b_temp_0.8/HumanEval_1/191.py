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
    paren_string = paren_string.strip()
    current_descendent = 0
    last_paren_end = 0
    for i in range(len(paren_string)):
        char = paren_string[i]
        if char == '(':
            stack.append({'end': i, 'current': 1})
            current_descendent += 1
            last_paren_end = i
        elif char == ')':
            stack.append({'end': i, 'current': -1})
            current_descendent -= 1
            if current_descendent == 0:
                break
    output = []
    last = None
    current = None
    for i in range(len(stack)):
        current = stack[i]['current']
        if last is None:
            output.append(paren_string[stack[i]['end'] + 1:stack[i]['end'] + 1 + stack[i]['current']])
        elif last == 1:
            if current == -1:
                output.append(paren_string[stack[i]['end'] + 1:])
            else:
                output.append(paren_string[stack[i]['end'] + 1:stack[i]['end']])
        else:
            assert last == -1
            output.append(paren_string[stack[i]['end'] + 1:stack[i]['end']])
        last = current
    return output

