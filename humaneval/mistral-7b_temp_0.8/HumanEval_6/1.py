from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # It is important to use a list here because we want to append to the list.
    # We do not want to reassign the original list.
    parsed_results = []
    # This is the count of the open parentheses in each group.
    count = 0
    for char in paren_string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            count = 0
        if count == 0:
            parsed_results.append(len(paren_string) - paren_string.index(char))
    return parsed_results
