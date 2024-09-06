from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    for i in range(1, len(paren_string)):
        if paren_string[i] == '(':
            level = (1 if paren_string[i-1] == ')' else 0) + 1
            j = i
            while j < len(paren_string):
                if paren_string[j] == ')':
                    level -= 1
                    if level == 0:
                        nested_parens.append(j - i + 1)
                        return nested_parens
                elif paren_string[j] == '(':
                    level += 1
                j += 1
        elif paren_string[i] == ')':
            j = i - 1
            level = 0
            while j >= 0:
                if paren_string[j] == '(':
                    level += 1
                if paren_string[j] == ')':
                    level -= 1
                    if level == 0:
                        nested_parens.append(i - j)
                        return nested_parens
                j -= 1
    if nested_parens:
        return [max(nested_parens)]
    return [0]

