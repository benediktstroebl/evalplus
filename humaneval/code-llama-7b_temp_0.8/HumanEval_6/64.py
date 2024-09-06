from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # break up the paren string into multiple groups
    paren_groups = paren_string.split(' ')
    # initialize an empty list to store the results
    results = []
    # loop through the groups
    for group in paren_groups:
        # initialize the deepest level of nesting
        deepest_level = 0
        # loop through the group
        for paren in group:
            # if '(' is found, increment the level of nesting
            if paren == '(':
                deepest_level += 1
            # if ')' is found, decrement the level of nesting
            elif paren == ')':
                deepest_level -= 1
        # append the deepest level to the list of results
        results.append(deepest_level)
    return results

