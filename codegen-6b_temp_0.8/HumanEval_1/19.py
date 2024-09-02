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
    str_list = []
    left, right = "({[", ")}]"
    for char in paren_string:
        if char in left:
            paren_stack.append(char)
        elif char in right:
            if char == ')' and len(paren_stack) > 0 and paren_stack[-1] == '(':
                paren_stack.pop()
            elif char == ']' and len(paren_stack) > 0 and paren_stack[-1] == '[':
                paren_stack.pop()
            elif char == '}' and len(paren_stack) > 0 and paren_stack[-1] == '{':
                paren_stack.pop()
            else:
                continue
        else:
            continue
        if len(paren_stack) > 0:
            str_list.append(''.join(paren_stack))
            paren_stack.clear()
    str_list.append(''.join(paren_stack))
    return str_list

