from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens = []
    depth = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        else:
            continue
        if depth == -1:
            break
    parens.append(depth)
    for i in range(1, i + 1):
        char = paren_string[:i]
        if char == '()':
            parens.append(2)
        elif char == '(()':
            parens.append(3)
        elif char == '(())':
            parens.append(4)
    max_depth = max(parens)
    # print(max_depth)
    return [max_depth] * len(parens)

