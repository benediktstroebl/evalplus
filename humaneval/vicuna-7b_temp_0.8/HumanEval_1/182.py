from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def count_open_braces(paren_group):
        count = 0
        for char in paren_group:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count

    def left_balance(paren_group):
        left = '('
        right = ')'
        count = 0
        for char in paren_group:
            if char == left:
                count += 1
            elif char == right:
                count -= 1
                if count < 0:
                    raise ValueError('Right bracket is not balanced')
        return count

    def right_balance(paren_group):
        left = '('
        right = ')'
        count = 0
        for char in reversed(paren_group):
            if char == left:
                count -= 1
            elif char == right:
                count += 1
                if count < 0:
                    raise ValueError('Left bracket is not balanced')
        return count

    return [paren_group for paren_group in zip(*[repeat(paren_string, i) for i in range(len(paren_string) + 1)]) if count_open_braces(paren_group) > 0]

example_input = '(() ()) (( )) ( ( ))'
