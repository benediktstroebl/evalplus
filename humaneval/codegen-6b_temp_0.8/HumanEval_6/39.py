from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_level = []
    nesting_level.append(0)
    stack = []
    for line in paren_string.split():
        if '(' in line:
            stack.append(line)
            nesting_level.append(0)
        elif ')' in line:
            stack.pop()
            if not stack:
                nesting_level.append(nesting_level[-1])
            else:
                while stack[-1][-1] != ')':
                    nesting_level.append(nesting_level[-1]+1)
                    stack.pop()
                stack.pop()
        else:
            try:
                line = int(line)
                nesting_level.append(line)
            except ValueError:
                continue

    return nesting_level[1:]

