from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # my own attempt
    # Stack = []
    # result = []
    # for char in paren_string:
    #     if char == "(":
    #         Stack.append(char)
    #     if char == ")":
    #         last_open_brace = Stack.pop()
    #         if not Stack:
    #             result.append(last_open_brace + char)
    #         else:
    #             last_open_brace += char
    #             Stack.append(last_open_brace)
    # return result

    # solution from book
    stack = []
    current = ""
    for c in paren_string:
        if c == "(":
            stack.append(current)
            current = ""
        elif c == ")":
            current += c
            if not stack:
                return []
            current = stack.pop() + current
        else:
            current += c
    return [current] if stack == [] else []

