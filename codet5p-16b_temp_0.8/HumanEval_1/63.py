from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    stack = []
    open_count = 0
    balanced = True
    separated_paren_groups = []
    for index, character in enumerate(paren_string):
        if character == '(':
            if open_count == 0:
                stack.append(index)
            open_count += 1
        if character == ')':
            open_count -= 1
            if open_count == 0:
                balanced = False
                for _ in range(stack.pop() + 1, index):
                    separated_paren_groups.append(paren_string[_])
                separated_paren_groups.append(character)
                stack.append(index)
    if balanced:
        separated_paren_groups.append(paren_string[stack.pop() + 1:])
    return separated_paren_groups
