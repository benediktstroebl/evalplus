from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # keep track of the maximum value of the number of nested parenthesis
    max_nested = 0

    # keep track of the current number of nested parenthesis
    cur_nested = 0

    # final list of nested levels
    nested_levels = []

    # iterate through all the characters of the string
    for c in paren_string:

        # if the character is '('
        if c == "(":

            # increase the number of nested parenthesis by 1
            cur_nested += 1

            # if the number of nested parenthesis is greater than the current maximum
            # update the maximum
            if cur_nested > max_nested:
                max_nested = cur_nested

        # if the character is ')'
        elif c == ")":

            # decrease the number of nested parenthesis by 1
            cur_nested -= 1

    # add the maximum value to the list of nested levels
    nested_levels.append(max_nested)

    # return the nested levels
    return nested_levels

