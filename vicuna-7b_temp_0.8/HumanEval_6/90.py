from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_list = []
    current_level = 0
    for open_paren in paren_string.strip("()").split("("):
        closed_paren = paren_string.rfind(")", 0) + 1
        nested_list.append(current_level)
        while closed_paren != -1:
            current_level = closed_paren
            closed_paren = paren_string.rfind(")", 0, closed_paren - len(open_paren)) + closed_paren
        nested_list.append(current_level)
    return nested_list

