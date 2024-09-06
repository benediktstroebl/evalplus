from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    list_ = []
    index = 0
    while index < len(paren_string):
        current_list = []
        paren_stack = []
        while index < len(paren_string):
            current_char = paren_string[index]
            if current_char == '(':
                paren_stack.append(current_char)
            elif current_char == ')':
                if not paren_stack:
                    break
                paren_stack.pop()
            current_list.append(current_char)
            index += 1
        list_.append(''.join(current_list))
    return list_

