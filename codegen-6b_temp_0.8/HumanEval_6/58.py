from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    res = []

    for paren in paren_string:
        if paren == '(':
            paren_stack.append('(')
        elif paren == ')':
            # check how deep the stack is
            depth = 0
            present = False
            while len(paren_stack) > 0:
                if paren_stack[-1] == '(':
                    depth += 1
                    paren_stack.pop()
                elif paren_stack[-1] == ')':
                    depth -= 1
                    present = True
                    break
                else:
                    present = True
            if present:
                # get the last element of the stack
                paren_stack.pop()

            if depth == 0:
                res.append(0)
            else:
                res.append(depth)

    return res

