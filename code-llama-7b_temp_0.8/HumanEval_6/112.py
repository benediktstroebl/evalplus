from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    deepest_level = 0
    group_deepest_levels = []

    # Algorithm
    # 1) Traverse the string char by char
    # 2) If the char is '(' then deepest_level is increased by 1
    # 3) If the char is ')' then deepest_level is decreased by 1
    # 4) If we hit a char where deepest_level is 0 and the last char was ')', then it is the end of a group
    #    and we need to save the deepest_level of the group so far in group_deepest_levels

    for char in paren_string:
        if char == '(':
            deepest_level += 1
        elif char == ')':
            deepest_level -= 1
        if deepest_level == 0 and char == ')':
            group_deepest_levels.append(deepest_level)

    return group_deepest_levels

