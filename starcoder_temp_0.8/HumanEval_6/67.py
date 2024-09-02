from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def find_max_depth(index, depth):
        if index >= len(paren_string) or paren_string[index] == ')':
            return depth

        if paren_string[index] == '(':
            left_depth = find_max_depth(index + 1, depth + 1)
            right_depth = find_max_depth(index + 2, depth)
            return max(left_depth, right_depth)

    return [find_max_depth(index, 0) for index in range(len(paren_string))]

