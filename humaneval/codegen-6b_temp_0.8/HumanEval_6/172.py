from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth = 0
    index_depth = 0
    max_depth = 0
    start_index = 0
    end_index = 0
    index_end_index = 0
    bracket_list = []
    for index, char in enumerate(paren_string):
        if char == '(':
            depth += 1
            if depth > max_depth:
                max_depth = depth
                start_index = index
        elif char == ')':
            depth -= 1
            if depth == 0:
                bracket_list.append([start_index, index+1])
                index_depth += 1
                index_end_index = index+1
    for group in bracket_list:
        bracket_list[index_depth] += [group[0],index_end_index]

    return [max_depth,*bracket_list]

