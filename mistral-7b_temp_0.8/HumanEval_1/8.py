from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def helper(string: str) -> str:
        new_string = ''
        open_braces_count = 0
        for index, char in enumerate(string):
            if char == '(':
                open_braces_count += 1
            elif char == ')':
                if open_braces_count > 0:
                    open_braces_count -= 1
                elif open_braces_count == 0:
                    return string[:index] + helper(string[index + 1:])
        return helper(string)

    result = helper(paren_string)
    return [result, helper(paren_string[1:])]

