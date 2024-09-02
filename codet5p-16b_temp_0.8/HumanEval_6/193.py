from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_depth = 0
    depth_list = []
    tmp_list = []
    paren_string = paren_string.replace(" ", "")

    for i in paren_string:
        if i == '(':
            tmp_list.append(i)
            max_depth += 1

        elif i == ')':
            tmp_list.pop()

            if tmp_list == []:
                depth_list.append(max_depth)

            max_depth = max_depth if tmp_list == [] else tmp_list[-1]

    return depth_list
