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
    last_pos = 0
    is_inside_parentheses = False
    for pos, char in enumerate(paren_string):
        if char == "(":
            is_inside_parentheses = True
        elif char == ")":
            is_inside_parentheses = False
            result.append(paren_string[last_pos:pos + 1])
            last_pos = pos + 1
        if is_inside_parentheses and char == " " and (pos == len(paren_string) - 1 or paren_string[pos + 1] != " "):
            return []
    return result

