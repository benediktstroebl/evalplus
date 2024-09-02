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
        return []

    stack = []
    i = 0
    while i < len(paren_string):
        c = paren_string[i]
        if not stack:
            stack.append(c)
            i += 1
        elif c == ')':
            count = 0
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    count += 1
                elif stack[-1] == ')':
                    if count == 0:
                        stack.pop()
                        break
                    else:
                        stack.pop()
                        count -= 1
            if not stack:
                result.append('')
            elif stack[-1] == '(':
                result.append('')
            else:
                result[-1] += ''.join(stack)
                stack = []
        else:
            stack.append(c)
            i += 1
    while stack:
        result.append(''.join(stack))
        stack = []
    return result

