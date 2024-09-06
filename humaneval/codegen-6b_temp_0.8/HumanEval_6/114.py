from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    open_paren_indices = []
    open_indices = []
    for i, char in enumerate(paren_string):
        if char == '(':
            open_paren_indices.append(i)
        elif char == ')':
            open_indices.append(i)
    max_nesting = 0
    for i, open_index in enumerate(open_indices):
        if open_index > max_nesting:
            max_nesting = open_index
    result = [max_nesting]
    for open_index in open_paren_indices:
        if open_index > result[0]:
            result[0] = open_index
        for j in range(1, len(result)):
            result[j] = max(result[j], open_index - result[j - 1])
    return result

