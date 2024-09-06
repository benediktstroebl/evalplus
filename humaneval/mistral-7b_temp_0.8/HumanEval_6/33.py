from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # convert input string to list
    parentheses_list = paren_string.split(" ")
    # create output list
    out = []
    for item in parentheses_list:
        # track the deepest level of nesting for the current item
        current_level = 0
        # track current position in the item
        current_pos = 0
        # keep track of the parentheses that were opened, to be closed later
        open_paren = 0
        # loop until end of the item
        while current_pos < len(item):
            # increment the current level of nesting if we find a left parentheses
            if item[current_pos] == "(":
                current_level += 1
                open_paren += 1
            # decrement the current level of nesting if we find a right parentheses
            elif item[current_pos] == ")":
                current_level -= 1
                open_paren -= 1
            # the level of nesting will be the maximum level of nesting
            # that was reached for the current item
