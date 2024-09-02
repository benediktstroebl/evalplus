from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    tokenizer = tokenize_string(paren_string)
    group_stack = []

    for token in tokenizer:
        if token == ')':
            if len(group_stack) == 0:
                return []
            else:
                group_stack.pop()

        elif token == '(':
            group_stack.append('')

    return [''.join(group_stack)]

