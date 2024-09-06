from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # The greedy algorithm keeps adding open paren to an array until it encounters a close paren.
    # Then, it removes all the elements in the array until it encounters the last open paren.
    # At that point, it keeps adding open paren to the array again.
    # This ensures that we have nested parenthesis all in a row and can then easily get the deepest level of nesting
    current_level = 0
    max_level = 0
    nums_to_print = []
    for char in paren_string:
        if char == "(":
            current_level += 1
        elif char == ")":
            max_level = max(max_level, current_level)
            current_level -= 1
        if char in ["(", ")"] and current_level == 0:
            nums_to_print.append(max_level)
            max_level = 0
    return nums_to_print

