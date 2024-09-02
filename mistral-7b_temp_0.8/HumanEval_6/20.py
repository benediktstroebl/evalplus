from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Run through all the groups
    # And return the max depth for each group
    result = []
    cur_depth = 0
    for group in paren_string.split(" "):
        if group == "":
            result.append(0)
            continue
        # Find the depth of the group
        max_depth = 0
        for paren in group:
            if paren == "(":
                cur_depth += 1
                max_depth = cur_depth
            elif paren == ")":
                cur_depth -= 1
                max_depth = cur_depth

        result.append(max_depth)

    return result

