from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_nested_parens_helper(paren_string: str) -> int:
        """ Given the substring of paren_string, return the deepest level of nesting of parentheses.

        >>> parse_nested_parens_helper('(()())')
        2
        >>> parse_nested_parens_helper('((())))')
        1
        """
        # First, find the deepest level of nesting for each pair of parentheses
        # O(n)
        pairs = []
        for i, c in enumerate(paren_string):
            if c == '(':
                pairs.append(i)
            elif c == ')':
                pairs.append(-i)

        # Then, take the maximum value of the above list of levels
        # O(n)
        return max(pairs)

    # O(n)
    return [parse_nested_parens_helper(group) for group in paren_string.split()]

