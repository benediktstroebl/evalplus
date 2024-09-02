from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    for paren in paren_string:
        if paren == '(':
            paren_stack.append(paren)
        elif paren == ')':
            prev_level = 0
            while paren_stack[-1] != '(':
                prev_level += 1
                paren_stack.pop()
            paren_stack.pop()
            prev_level = max(prev_level, 1)
            for i in range(len(paren_stack) - 1, -1, -1):
                if paren_stack[i] == '(':
                    paren_stack[i] = prev_level + 1
                    break
    return paren_stack

