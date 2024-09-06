from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    if not paren_string:
        return [paren_string]

    brace_count = 1
    paren_stack = list()
    stack_top = None
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            if stack_top is None:
                stack_top = i
            brace_count += 1
        elif paren_string[i] == ')':
            if not paren_stack or paren_stack[-1] != '(':
                raise ValueError('unbalanced bracket')
            brace_count -= 1
            paren_stack.pop()
            stack_top = None
        elif paren_string[i].isspace():
            i += 1
            continue
        else:
            if paren_stack and paren_stack[-1] == '(':
                brace_count -= 1
            if not stack_top or paren_string[stack_top] != '(':
                stack_top = i
            if not paren_stack or paren_stack[-1] != '(':
                paren_stack.append(paren_string[stack_top:i + 1])

        i += 1

    if not paren_stack:
        return [paren_string]

    if bracket_count != 0:
        raise ValueError('unbalanced bracket')
    elif stack_top is None:
        raise ValueError('unbalanced bracket')

    i = 0
    while i < len(paren_stack):
        if paren_stack[i] == '(':
            paren_stack[i] = paren_string[stack_top:i]
        i += 1

    return paren_stack

