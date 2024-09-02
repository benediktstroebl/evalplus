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
    stack = []
    for char in paren_string:
        # If there's an open bracket, add it to the stack
        if char == '(':
            stack.append('(')
        elif char == ')':
            # We've processed all groupings in this layer, so we need to add them to our result and stack
            # to be processed next
            if stack == []:
                result.append('')
            else:
                while stack[-1] != '(':
                    # Add the last closed group to our result
                    result.append(stack.pop())
                    if len(stack) < 1:
                        break
                # pop the last open bracket from the stack
                stack.pop()

    # If there's anything left in the stack (which should never happen because we looped through all
    # characters and never added anything to the result list), add it to the result list
    if stack:
        result.append(stack[-1])

    return result

