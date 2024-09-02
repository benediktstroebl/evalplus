from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # This is a stack-based parsing, you have a current level of nesting and a total number of nesting.
    # If you see a '(' you increment the current level.
    # When you see a ')' you increment the total and current level.
    # At the end, you return the total level.
    total_level = []
    curr_level = []
    for paren in paren_string:
        if paren == '(':
            curr_level.append(1)
        elif paren == ')':
            total_level.append(sum(curr_level) + 1)
            curr_level.pop()
    return total_level

