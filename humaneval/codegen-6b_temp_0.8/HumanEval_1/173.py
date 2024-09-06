from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    num_brackets = 0
    final_list = []

    def is_balanced(paren_group):
        nonlocal num_brackets
        num_brackets += paren_group.count('(')
        num_brackets -= paren_group.count(')')
        return num_brackets == 0

    def is_open(char: str):
        return char == '('

    def is_close(char: str):
        return char == ')'

    paren_group = ''
    for ch in paren_string:
        if ch == '(':
            if is_open(paren_group[-1]):
                paren_group += ch
            else:
                paren_group += ch
                final_list.append(paren_group)
                paren_group = ''
        elif ch == ')':
            if is_balanced(paren_group):
                paren_group += ch
            else:
                paren_group += ch
                final_list.append(paren_group)
                paren_group = ''
        elif ch != ' ':
            paren_group += ch

    if is_balanced(paren_group):
        final_list.append(paren_group)
    else:
        final_list.append(paren_group)

    final_list = [x[1:-1] for x in final_list]
    return final_list

