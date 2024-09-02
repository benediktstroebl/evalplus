from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens = 0
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append(parens)
            parens += 1
        elif char == ')':
            parens -= 1
            if parens == 0:
                # This is the last opening parenthesis, so we can remove the entire stack
                stack.pop()
                parens = stack[-1]
        elif char == ' ':
            if not stack:
                # This is the first opening parenthesis of a new group, so we add it to the stack
                stack.append(parens)
                parens += 1
            else:
                # Otherwise, we add the current character to the current level of the stack
                stack[-1].append(char)
    return [len(x) for x in stack]