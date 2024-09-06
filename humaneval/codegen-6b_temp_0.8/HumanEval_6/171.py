from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    stack = []
    indices = []

    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return indices
            current_depth = len(stack)
            while stack[-1] != '(':
                last_item = stack.pop()
                current_depth -= 1
                max_depth = max(current_depth, max_depth)
                indices.append(i - (len(stack) + 1) + current_depth)
            stack.pop()

    return indices

