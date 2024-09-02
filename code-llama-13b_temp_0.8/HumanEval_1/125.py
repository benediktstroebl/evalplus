from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []  # for keeping the processed parens
    process_stack = []  # for keeping the unprocessed parens
    for paren in paren_string:
        if paren == '(':
            process_stack.append(paren)
        elif paren == ')':
            if process_stack:
                process_stack.pop()
                paren_stack.append(paren)
        elif paren == ' ':
            continue
        else:
            raise ValueError('Invalid character in string')

    if process_stack:
        raise ValueError('Parentheses are not balanced')

    if len(paren_stack) == 1:
        return [paren_stack[0]]

    result = []
    for i in range(len(paren_stack)):
        if paren_stack[i] == '(':
            result.append(paren_stack[i])
            j = i + 1
            while True:
                if paren_stack[j] == '(':
                    result.append(paren_stack[j])
                elif paren_stack[j] == ')':
                    result.append(paren_stack[j])
                    result.append(' ')
                    break
                else:
                    raise ValueError('Parentheses are not balanced')
                j += 1
    return "".join(result).split()

