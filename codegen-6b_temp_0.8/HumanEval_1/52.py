from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    #   Set up resulting strings
    new_list = []

    #   Create a stack to track parentheses positions
    stack = []

    #   Populate the stack with a starting open bracket
    stack.append([stack])

    #   Iterate over the characters in the input string and find corresponding closing brackets
    for char in paren_string:
        if char == '(':
            stack.append([stack])
        elif char == ')':
            try:
                last_element = stack.pop()
                stack[-1].append(last_element)
            except IndexError:
                pass
        else:
            continue

    #   Iterate over the elements in the stack and pop the corresponding open parenthesis
    while len(stack) > 0:
        element = stack.pop()
        if isinstance(element, list):
            new_list.append(''.join(element))
        else:
            new_list.append(''.join(list(element)))

    return new_list

