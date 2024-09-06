from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Intuition:
    # 1. Find the start index of first parentheses
    # 2. Walk until we find a closing parenthesis
    # 3. Repeat steps 1 and 2
    # 4. Return the max depth of each group as a list
    return [max_depth(i) for i in paren_string.split()]

