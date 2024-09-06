from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_group(string: str):
        count = 0
        for char in string:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
        return count

    nested_parens = []
    for group in paren_string.split(" "):
        nested_parens.append(parse_group(group))
    return nested_paren
