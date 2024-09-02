from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    final_list = []
    for line in paren_string.split(' '):
        level = 0
        for i in range(len(line)):
            if line[i] == '(':
                level += 1
            elif line[i] == ')':
                level -= 1
            if level == -1:
                final_list.append(i + 1)
                break
    return final_list
