from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return_list = []
    for paren in paren_string:
        if paren in ('(', ')'):
            return_list.append(paren)
        elif paren == '(':
            stack_count = 1
            new_paren = '('
            while stack_count:
                if paren == '(':
                    stack_count += 1
                if paren == ')':
                    stack_count -= 1
                new_paren += paren
                paren = new_paren
            return_list.append(new_paren)
    return return
