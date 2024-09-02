from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_single_group(group_string: str) -> int:
        """ Parses a single group of nested parentheses. E.g. ()() returns 2."""
        max_depth = 0
        current_depth = 0
        for char in group_string:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        return max_depth

    return [parse_single_group(s) for s in paren_string.split()]

