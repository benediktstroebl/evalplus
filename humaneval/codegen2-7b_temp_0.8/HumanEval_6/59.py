from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return [
        len(set(
            paren_string[index:index + len(paren)]
            for paren in paren_string
            for index in range(len(paren_string))
            if paren_string[index] == paren
        ))
        for paren in ('()', '()()', '(())', '()()()')
    
