from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []

    def balance(paren_string: str):
        """ Return the index of the next unbalanced closing parenthesis
        >>> balance('(()(')
        5
        """
        balance_count = 0
        for i, c in enumerate(paren_string):
            if c == '(':
                balance_count += 1
            elif c == ')':
                balance_count -= 1
                if balance_count == 0:
                    return i

    stack = []
    for i, c in enumerate(paren_string):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack) == 0:
                raise ValueError("Unbalanced closing parenthesis at position {}".format(i))
            result.append(paren_string[stack.pop():i + 1])

    if len(stack) != 0:
        raise ValueError("Unbalanced opening parenthesis at position {}".format(stack.pop()))

    return result

