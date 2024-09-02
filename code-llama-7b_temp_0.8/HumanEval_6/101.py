from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_nesting = 0
    max_nesting_list = []
    for group in paren_string.split():
        stack_open_count = 0
        for i in range(len(group)):
            if group[i] == '(':
                stack_open_count += 1
            elif group[i] == ')':
                stack_open_count -= 1
            if stack_open_count >= max_nesting:
                max_nesting = stack_open_count
        max_nesting_list.append(max_nesting)
        max_nesting = 0
    return max_nesting_list

