from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string.count('(')!= paren_string.count(')'):
        return []

    queue = [paren_string]
    sep_strings = []
    while len(queue) > 0:
        current_string = queue.pop()
        if is_balanced(current_string):
            sep_strings.append(current_string)
        else:
            for i in range(len(current_string)):
                if current_string[i] == '(':
                    queue.insert(0, current_string[:i] + current_string[i + 1:])
    return sep_strings

