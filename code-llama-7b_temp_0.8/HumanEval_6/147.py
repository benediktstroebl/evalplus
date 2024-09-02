from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # First get the level of nesting for each group
    # level_of_nesting = [len(x) for x in paren_string.split()]
    level_of_nesting = []

    for group in paren_string.split():
        open_parens_counter = 0
        close_parens_counter = 0
        max_parens_level = 0
        for paren in group:
            if paren == "(":
                open_parens_counter += 1
            elif paren == ")":
                close_parens_counter += 1
            max_parens_level = max(max_parens_level, open_parens_counter)
        # If the number of open and close parentheses are the same,
        # it means the parentheses are balanced
        # Otherwise, the open parentheses are greater than the close parentheses
        level_of_nesting.append(max_parens_level - close_parens_counter)

    return level_of_nesting

