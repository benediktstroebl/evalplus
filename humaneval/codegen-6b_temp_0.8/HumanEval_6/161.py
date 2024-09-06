from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = [0]
    max_seq = 0
    max_level = 0
    for c in paren_string:
        if c == '(':
            stack.append(0)
            max_seq = max(max_seq, stack[-1])
        elif c == ')':
            if len(stack) == 1:
                return [-1]
            popped = stack.pop()
            stack[-1] = popped + 1
            max_seq = max(max_seq, stack[-1])
    return [-1] if len(stack) == 1 else [stack[-1]]

