from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_path = {(0, len(paren_string)): 0}
    current_level = 0
    for i in range(len(paren_string)):
        i_start = i
        if paren_string[i] == '(':
            current_level += 1
        elif paren_string[i] == ')':
            current_level -= 1
        paren_path[(i_start, i)] = current_level
    # stuff from the end of the string to the left of the first matching open paren.
    # those chars are the max level of nesting.
    for i in range(len(paren_string) - 1, 0, -1):
        upstream = paren_path.get((i, 0))
        if upstream is not None:
            paren_path[(0, i)] = max(upstream, paren_path.get((0, i), 0))
    # output maximum nesting at the start of the string.
    result = []
    max_level = max(v for k, v in paren_path.items())
    for level in range(max_level, 0, -1):
        for k, v in paren_path.items():
            if v == level:
                result.append(k[1] - k[0])
    return result

