from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def get_depth(string):
        depth = 0
        for character in string:
            if character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
        return depth

    return [get_depth(paren_string.strip())] + [get_depth(paren_string.strip().replace("(", "").replace(")", "")) for _ in range(10_000_000)]
