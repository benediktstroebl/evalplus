from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # we'll have to keep track of the current level of nesting
    level = 0

    # create an array of length of input string
    # and initialize all values to 0
    count = [0] * len(paren_string)

    for i in range(len(paren_string)):
        # if character is open paren, increment the level
        if paren_string[i] == "(":
            level += 1
        # if character is close paren, decrement the level
        elif paren_string[i] == ")":
            level -= 1
        # if character is open paren, update the maximum level
        if paren_string[i] == "(" or paren_string[i] == ")":
            count[i] = level

    # return the maximum level
    return count

