from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # 1. Add each open paren to a stack
    # 2. If stack is not empty, pop stack and add closed paren
    # 3. Append current stack to result list
    # 4. Return result list

    # TODO: Implement this function!
    result_list = []
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
                result_list.append(''.join(stack))
                stack = []
    result_list.append(''.join(stack))
    return result_list

