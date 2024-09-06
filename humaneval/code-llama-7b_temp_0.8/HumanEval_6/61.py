from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # the deepest level of nesting for a given string in the input
    deepest_nest = 0
    # the output for the input
    result = []

    for group in paren_string.split():
        # the deepest level of nesting for a given group
        curr_nest = 0
        for char in group:
            # increment the level of nesting when '(' is encountered
            if char == "(":
                curr_nest += 1
            # decrease the level of nesting when ')' is encountered
            elif char == ")":
                curr_nest -= 1
        # update the result with the new level of nesting
        result.append(curr_nest)
        # update the deepest level of nesting if the current level is greater
        if curr_nest > deepest_nest:
            deepest_nest = curr_nest
    return [nest + deepest_nest for nest in result]

