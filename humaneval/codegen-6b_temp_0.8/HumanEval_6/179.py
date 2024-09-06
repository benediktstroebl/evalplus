from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_count = 0
    
    for index, ch in enumerate(paren_string):
        if ch == '(':
            count = count_nested_parens(paren_string, index)
            if count > max_count:
                max_count = count
    
    return [max_count]
