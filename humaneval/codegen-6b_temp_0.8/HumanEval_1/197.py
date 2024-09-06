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
    for i in range(len(paren_string)):
        curr_char = paren_string[i]
        if curr_char == ")":
            paren_chars = []
            while len(stack) > 0 and stack[-1] != "(":
                paren_chars.append(stack.pop())
            # If we don't have any open parens, return list of paranthesis
            if len(stack) == 0:
                result.append(''.join(paren_chars)[::-1])
            # If we have an open paren that we need to close, just pop the open bracket
            else:
                stack.pop()
        elif curr_char == "(":
            stack.append(curr_char)
        elif curr_char != " ":
            stack.append(curr_char)
    while len(stack) > 0:
        result.append(''.join(stack))
        stack.pop()
    return result

