from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # ------------------------------------------------------------------
    def count_parens(paren_string: str) -> int:
        """ Input to this function is a string that may contain any number of nested parentheses.
        Output the deepest level of nesting of parentheses.

        >>> count_parens('(()()) ((())) () ((())()())')
        3
        """
        # ------------------------------------------------------------------
        # Replace every pair of parentheses with a single character and count the number of parentheses
        # E.g. for '((())) (()) (())' output 4
        return len([c for c in paren_string.replace('()', '')])

    # ------------------------------------------------------------------
    return [count_parens(paren_group) for paren_group in paren_string.split(' ')]

