from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # So the only time when the stack is empty, we have a valid end of the string.
    # So we need to keep track of the max_level at that point.
    # But the moment we pop an element off the stack, we can't know the level of the max nesting, so we need to keep track of that as well
    max_level = 0
    max_level_at_empty_stack = 0

    stack = []
    for ch in paren_string:
        if ch == '(':
            stack.append(ch)
            if len(stack) > max_level:
                max_level = len(stack)
        elif ch == ')':
            if len(stack) == 0:
                max_level_at_empty_stack = max_level
            else:
                stack.pop()
                if len(stack) > max_level:
                    max_level = len(stack)
    return [max_level_at_empty_stack] * len(paren_string.split())

