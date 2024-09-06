from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    r = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            stack = []
            start = i + 1
            end = i
            level = 0
            while end < len(paren_string):
                if paren_string[end] == '(':
                    stack.append(end)
                    level += 1
                elif paren_string[end] == ')':
                    if stack:
                        start = stack.pop() + 1
                        level -= 1
                        end = stack[-1] if stack else -1
                    else:
                        return None
                else:
                    end += 1
                
            if level == 0:
                start -= 1
                r.append(end - start)
            else:
                r.append(level)
    return r

