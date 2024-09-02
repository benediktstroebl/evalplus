from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    def process(paren_string: str) -> int:
        # base case for the empty string
        if not paren_string:
            return 0

        # recurse on the left and right side of the first opening paren
        first_open_paren = paren_string.find('(')
        left_count = process(paren_string[:first_open_paren])
        right_count = process(paren_string[first_open_paren + 1:])

        # count opening and closing parens to get the maximum depth of nesting
        return max(left_count, right_count) + 1

    return [process(paren_string) for paren_string in paren_string.split()]

