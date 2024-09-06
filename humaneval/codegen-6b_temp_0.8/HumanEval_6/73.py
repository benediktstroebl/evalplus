from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # start with an empty list for each level of nesting
    curr_level = []
    # list to hold the final level of nesting
    final_levels = []
    # iterate over the parenthesis string, adding the pars to their respective nesting level
    for p in paren_string:
        if p == '(':
            curr_level.append(1)
        if p == ')':
            # if current level of nesting is empty, then this level of nesting is empty
            if not curr_level:
                # add 1 to the previous level in the final level to count the nesting level
                final_levels.append(1)
            else:
                curr_level.pop()
    # flatten the final list of nesting levels
    final_levels = [item for sublist in final_levels for item in sublist]
    return final_levels

