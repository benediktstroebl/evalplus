from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Hint1: if you think of this problem as parsing the input string, you'll probably want to use a stack
    # Hint2: keep in mind that you want to separate groups. Keeping track of the last "break" in the string
    # will be important
    stack, groups, last_break = [], [], 0
    for index, paren in enumerate(paren_string.replace(' ', '')):
        if paren == '(':
            stack.append(index)
        elif paren == ')':
            group_start = stack.pop()
            groups.append(paren_string[group_start:index + 1])
            last_break = index + 1
    return groups

