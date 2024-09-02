from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_stack = []
    output_list = []

    for char in paren_string:
        if char == '(':
            max_stack.append(1)
        else:
            last_max = max_stack.pop()
            max_stack.append(last_max + 1)
            output_list.append(max_stack[-1])
    return output_list

