from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # init stack and return_list
    stack: List = []
    return_list: List = []
    # separate the string by characters
    split_string: List = list(paren_string)
    # init open brace counter
    open_braces: int = 0

    for character in split_string:
        # push open braces into the stack
        if character == '(':
            stack.append(character)
            open_braces += 1
        # pop from stack when closing braces is found
        elif character == ')':
            stack.pop()
            open_braces -= 1
        # if the stack is empty and you're at a close brace, start a new group
        if character == ')' and open_braces == 0:
            return_list.append("".join(stack))
            stack = []

    # if the stack is empty, you're done. Return your list.
    if len(stack) == 0:
        return return_list
    # otherwise, you didn't have enough closing braces for the number of open ones. Return error
    else:
        return "Error"

