from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parenthesis_list = []
    parenthesis_stack = []
    paren_index = 0
    in_parenthesis = False
    while paren_index < len(paren_string):
        current_char = paren_string[paren_index]
        if current_char == '(':
            if in_parenthesis == False:
                parenthesis_stack.append(paren_index)
                in_parenthesis = True
            else:
                parenthesis_stack.pop()
        elif current_char == ')':
            if in_parenthesis == False:
                parenthesis_stack.append(paren_index)
                in_parenthesis = True
            else:
                parenthesis_stack.pop()
        elif current_char == ' ':
            paren_index += 1
        else:
            paren_index += 1

        if in_parenthesis == False and len(parenthesis_stack) == 0:
            parenthesis_list.append(paren_string[paren_index - len(parenthesis_stack) - 1:
